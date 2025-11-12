import json
import logging
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import requests

from src.services.proxy_manager import ProxyManager
from src.services.request_throttler import RequestThrottler

LOGGER = logging.getLogger(__name__)

@dataclass
class SpyfuClient:
    base_url: str
    api_key: Optional[str] = None
    proxy_manager: Optional[ProxyManager] = None
    throttler: Optional[RequestThrottler] = None
    use_sample_data: bool = True
    timeout: int = 20

    def _get_proxies(self) -> Optional[Dict[str, str]]:
        if not self.proxy_manager:
            return None
        proxy_url = self.proxy_manager.get_proxy()
        if not proxy_url:
            return None
        return {
            "http": proxy_url,
            "https": proxy_url,
        }

    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> Any:
        if self.use_sample_data or not self.api_key:
            LOGGER.debug(
                "Using sample data mode for endpoint=%s domain=%s",
                endpoint,
                params.get("domain"),
            )
            return self._fake_response(endpoint, params)

        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = {"User-Agent": "SpyfuBulkUrlsClient/0.1.0"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        if self.throttler:
            self.throttler.acquire()

        proxies = self._get_proxies()
        LOGGER.debug("Requesting %s with params=%s", url, params)
        resp = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
            proxies=proxies,
        )
        resp.raise_for_status()

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            return resp.json()
        try:
            return json.loads(resp.text)
        except json.JSONDecodeError:
            LOGGER.warning(
                "Non-JSON response from SpyFu for %s. Returning raw text snippet.",
                endpoint,
            )
            return {"raw": resp.text[:1000]}

    def _fake_response(self, endpoint: str, params: Dict[str, Any]) -> Any:
        domain = params.get("domain", "example.com")
        country = params.get("country", "US")
        seed = hash((endpoint, domain, country, int(time.time()) // 3600)) & 0xFFFF

        def pseudo_rand(n: int) -> float: