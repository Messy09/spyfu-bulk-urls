import csv
import json
import logging
import os
from typing import Any, Dict, Iterable, List

LOGGER = logging.getLogger(__name__)

def _ensure_dir(path: str) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def _flatten_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Flatten nested arrays/objects to JSON strings for CSV export.
    """
    flat: Dict[str, Any] = {}
    for key, value in record.items():
        if isinstance(value, (dict, list)):
            flat[key] = json.dumps(value, ensure_ascii=False)
        else:
            flat[key] = value
    return flat

def export_to_json(records: Iterable[Dict[str, Any]], output_path: str) -> None:
    _ensure_dir(output_path)
    data = list(records)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    LOGGER.info("Wrote JSON output to %s", output_path)

def export_to_csv(records: Iterable[Dict[str, Any]], output_path: str) -> None:
    _ensure_dir(output_path)
    data = list(records)
    if not data:
        LOGGER.warning("No records to export to CSV.")
        return

    flattened = [_flatten_record(r) for r in data]
    fieldnames: List[str] = sorted(flattened[0].keys())

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in flattened:
            writer.writerow(row)
    LOGGER.info("Wrote CSV output to %s", output_path)

def export_records(records: Iterable[Dict[str, Any]], output_path: str, fmt: str = "json") -> None:
    fmt = fmt.lower()
    if fmt == "json":
        export_to_json(records, output_path)
    elif fmt == "csv":
        export_to_csv(records, output_path)
    else:
        raise ValueError(f"Unsupported export format: {fmt}")