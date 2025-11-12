import logging
import time
from typing import Any, Dict, Optional

from src.services.spyfu_client import SpyfuClient
from src.parsers.json_normalizer import build_record

LOGGER = logging.getLogger(__name__)

class AdsProcessor:
    def __init__(self, client: SpyfuClient) -> None:
        self.client = client

    def process(
        self,
        origin: str,
        domain: str,
        country: Optional[str],
        run_id: str,
    ) -> Dict[str, Any]:
        LOGGER.debug("Fetching top ads for %s", domain)
        ads = self.client.get_top_ads(domain, country)

        record = build_record(
            origin=origin,
            domain=domain,
            country=country,
            process_type="top_ads",
            top_competitors=[],
            most_valuable_keywords=[],
            most_successful_keywords=[],
            newly_ranked_keywords=[],
            top_ads=ads,
            domain_stats={},
            timestamp_ms=int(time.time() * 1000),
            run_id=run_id,
            notes=None,
        )
        return record