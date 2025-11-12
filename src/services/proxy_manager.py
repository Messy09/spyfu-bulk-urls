import itertools
import logging
from typing import Dict, Iterable, Optional

LOGGER = logging.getLogger(__name__)

class ProxyManager:
    """
    Simple round-robin proxy manager.

    Expected configuration format:

    {
        "http": ["http://user:pass@host:port", "..."],
        "https": ["http://user:pass@host:port", "..."]
    }

    Or:

    {
        "rotating": [
            "http://user:pass@host1:port",
            "http://user:pass@host2:port"
        ]
    }
    """

    def __init__(self, config: Dict) -> None:
        self._proxies: Iterable[str] = []
        self._it: Optional[Iterable[str]] = None

        if not config:
            LOGGER.info("ProxyManager initialized without proxies.")
            return

        if "rotating" in config:
            self._proxies = list(config.get("rotating") or [])
        else:
            urls = set()
            for key in ("http", "https"):
                urls.update(config.get(key) or [])
            self._proxies = list(urls)

        if self._proxies:
            LOGGER.info("ProxyManager loaded %d proxies.", len(self._proxies))
            self._it = itertools.cycle(self._proxies)
        else:
            LOGGER.info("ProxyManager received empty proxy list.")

    def get_proxy(self) -> Optional[str]:
        if not self._it:
            return None
        proxy = next(self._it)
        LOGGER.debug("Using proxy: %s", proxy)
        return proxy