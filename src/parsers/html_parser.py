import json
import logging
import re
from typing import Any, Optional

LOGGER = logging.getLogger(__name__)

JSON_BLOCK_RE = re.compile(r"(\{.*\})", re.DOTALL)

def extract_json_from_html(html: str) -> Any:
    """
    Very small helper that tries to extract the first JSON object from an HTML document.

    This is a fallback for cases where SpyFu exposes JSON inside script tags.
    """
    match = JSON_BLOCK_RE.search(html)
    if not match:
        LOGGER.debug("No JSON block found in HTML.")
        return {}

    block = match.group(1)
    try:
        return json.loads(block)
    except json.JSONDecodeError:
        LOGGER.warning("Failed to decode JSON block from HTML snippet.")
        return {}