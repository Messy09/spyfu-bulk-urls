import logging
import time
from typing import Any, Dict, List, Optional

from src.services.spyfu_client import SpyfuClient
from src.parsers.json_normalizer import build_record

LOGGER = logging.getLogger(__name__)

class KeywordsProcessor:
    def __init__(self, client: SpyfuClient) -> None:
        self.client = client

    def _derive_successful_keywords(self, valuable_keywords: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # For demo purposes, treat top N valuable keywords as "most successful"
        top = sorted(
            valuable_keywords,
            key=lambda k: k.get("estimated_value", 0),
            reverse=True,
        )
        return top[:3]

    def process_most_valuable(
        self,
        origin: str,
        domain: str,
        country: Optional[str],
        run_id: str,
    ) -> Dict[str, Any]:
        LOGGER.debug("Fetching most valuable keywords for %s", domain)
        valuable = self.client.get_most_valuable_keywords(domain, country)
        successful = self._derive_successful_keywords(valuable)

        record = build_record(
            origin=origin,
            domain=domain,
            country=country,
            process_type="most_valuable_keywords",
            top_competitors=[],
            most_valuable_keywords=valuable,
            most_successful_keywords=successful,
            newly_ranked_keywords=[],
            top_ads=[],
            domain_stats={},
            timestamp_ms=int(time.time() * 1000),
            run_id=run_id,
            notes=None,
        )
        return record

    def process_newly_ranked(
        self,
        origin: str,
        domain: str,
        country: Optional[str],
        run_id: str,
    ) -> Dict[str, Any]:
        LOGGER.debug("Fetching newly ranked keywords for %s", domain)
        newly_ranked = self.client.get_newly_ranked_keywords(domain, country)

        record = build_record(
            origin=origin,
            domain=domain,
            country=country,
            process_type="newly_ranked_keywords",
            top_competitors=[],
            most_valuable_keywords=[],
            most_successful_keywords=[],
            newly_ranked_keywords=newly_ranked,
            top_ads=[],
            domain_stats={},
            timestamp_ms=int(time.time() * 1000),
            run_id=run_id,
            notes=None,
        )
        return record