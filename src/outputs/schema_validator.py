import logging
from typing import Any, Dict, Iterable, List

from jsonschema import Draft7Validator

LOGGER = logging.getLogger(__name__)

RECORD_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "required": [
        "origin",
        "domain",
        "country",
        "process_type",
        "top_competitors",
        "most_valuable_keywords",
        "most_successful_keywords",
        "newly_ranked_keywords",
        "top_ads",
        "domain_stats",
        "timestamp",
        "run_id",
    ],
    "properties": {
        "origin": {"type": "string"},
        "domain": {"type": "string"},
        "country": {"anyOf": [{"type": "string"}, {"type": "null"}]},
        "process_type": {"type": "string"},
        "top_competitors": {"type": "array"},
        "most_valuable_keywords": {"type": "array"},
        "most_successful_keywords": {"type": "array"},
        "newly_ranked_keywords": {"type": "array"},
        "top_ads": {"type": "array"},
        "domain_stats": {"type": "object"},
        "timestamp": {"type": "number"},
        "run_id": {"type": "string"},
        "notes": {"anyOf": [{"type": "string"}, {"type": "null"}]},
    },
    "additionalProperties": True,
}

def validate_records(records: Iterable[Dict[str, Any]]) -> None:
    data: List[Dict[str, Any]] = list(records)
    validator = Draft7Validator(RECORD_SCHEMA)
    errors: List[str] = []

    for idx, record in enumerate(data):
        for error in validator.iter_errors(record):
            errors.append(f"Record #{idx}: {error.message}")

    if errors:
        for e in errors:
            LOGGER.error("Schema validation error: %s", e)
        raise ValueError(f"Schema validation failed for {len(errors)} field(s).")