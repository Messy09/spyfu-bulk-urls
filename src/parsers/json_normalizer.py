import time
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

def normalize_domain(url: str) -> str:
    """
    Normalize input URL to a root domain.
    """
    parsed = urlparse(url.strip())
    if not parsed.scheme:
        parsed = urlparse("https://" + url.strip())

    host = parsed.hostname or ""
    if host.startswith("www."):
        host = host[4:]
    return host or url.strip()

def build_record(
    origin: str,
    domain: str,
    country: Optional[str],
    process_type: str,
    top_competitors: List[Dict[str, Any]],
    most_valuable_keywords: List[Dict[str, Any]],
    most_successful_keywords: List[Dict[str, Any]],
    newly_ranked_keywords: List[Dict[str, Any]],
    top_ads: List[Dict[str, Any]],
    domain_stats: Dict[str, Any],
    timestamp_ms: Optional[int] = None,
    run_id: Optional[str] = None,
    notes: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Build a normalized record matching the README example schema.
    """
    if timestamp_ms is None:
        timestamp_ms = int(time.time() * 1000)

    record: Dict[str, Any] = {
        "origin": origin,
        "domain": domain,
        "country": country,
        "process_type": process_type,
        "top_competitors": top_competitors or [],
        "most_valuable_keywords": most_valuable_keywords or [],
        "most_successful_keywords": most_successful_keywords or [],
        "newly_ranked_keywords": newly_ranked_keywords or [],
        "top_ads": top_ads or [],
        "domain_stats": domain_stats or {},
        "timestamp": int(timestamp_ms),
        "run_id": run_id or "",
        "notes": notes,
    }
    return record