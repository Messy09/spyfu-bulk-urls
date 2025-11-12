import argparse
import json
import logging
import logging.config
import os
import time
from typing import Any, Dict, Iterable, List, Optional

from src.services.spyfu_client import SpyfuClient
from src.services.proxy_manager import ProxyManager
from src.services.request_throttler import RequestThrottler
from src.processors.competitors_processor import CompetitorsProcessor
from src.processors.keywords_processor import KeywordsProcessor
from src.processors.ads_processor import AdsProcessor
from src.processors.domain_stats_processor import DomainStatsProcessor
from src.outputs.exporters import export_records
from src.outputs.schema_validator import validate_records
from src.parsers.json_normalizer import normalize_domain

LOGGER = logging.getLogger(__name__)

def configure_logging(log_config_path: str) -> None:
    if os.path.exists(log_config_path):
        logging.config.fileConfig(log_config_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        )

def load_settings(settings_path: Optional[str]) -> Dict[str, Any]:
    if not settings_path:
        return {}

    if not os.path.exists(settings_path):
        LOGGER.warning("Settings file %s not found, using defaults.", settings_path)
        return {}

    with open(settings_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as exc:
            LOGGER.error("Failed to parse settings file %s: %s", settings_path, exc)
            return {}

def read_urls_from_file(path: str) -> List[str]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input URLs file not found: {path}")

    urls: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)

    if not urls:
        raise ValueError(f"No URLs found in input file: {path}")

    return urls

def build_spyfu_client(settings: Dict[str, Any]) -> SpyfuClient:
    base_url = settings.get("spyfu_base_url", "https://www.spyfu.com")
    api_key = settings.get("spyfu_api_key") or os.getenv("SPYFU_API_KEY")
    use_sample_data = settings.get("use_sample_data", True)
    timeout = int(settings.get("timeout_seconds", 20))

    proxy_cfg = settings.get("proxies") or {}
    proxy_manager = ProxyManager(proxy_cfg)

    rpm = int(settings.get("requests_per_minute", 60))
    throttler = RequestThrottler(rate_per_minute=rpm)

    client = SpyfuClient(
        base_url=base_url,
        api_key=api_key,
        proxy_manager=proxy_manager,
        throttler=throttler,
        use_sample_data=use_sample_data,
        timeout=timeout,
    )
    return client

def process_urls(
    urls: Iterable[str],
    country: Optional[str],
    process_type: str,
    settings: Dict[str, Any],
) -> List[Dict[str, Any]]:
    client = build_spyfu_client(settings)

    competitors_processor = CompetitorsProcessor(client)
    keywords_processor = KeywordsProcessor(client)
    ads_processor = AdsProcessor(client)
    domain_stats_processor = DomainStatsProcessor(client)

    processors = {
        "top_competitors": competitors_processor,
        "most_valuable_keywords": keywords_processor,
        "newly_ranked_keywords": keywords_processor,
        "top_ads": ads_processor,
        "domain_stats": domain_stats_processor,
    }

    if process_type not in processors:
        raise ValueError(
            f"Unsupported process_type '{process_type}'. "
            f"Supported types: {', '.join(sorted(processors.keys()))}"
        )

    processor = processors[process_type]
    run_id = f"spyfu-bulk-urls-{int(time.time())}"
    records: List[Dict[str, Any]] = []

    for url in urls:
        domain = normalize_domain(url)
        LOGGER.info("Processing %s (%s) for %s", url, domain, process_type)
        try:
            if process_type == "top_competitors":
                record = competitors_processor.process(
                    origin=url,
                    domain=domain,
                    country=country,
                    run_id=run_id,
                )
            elif process_type == "most_valuable_keywords":
                record = keywords_processor.process_most_valuable(
                    origin=url,
                    domain=domain,
                    country=country,
                    run_id=run_id,
                )
            elif process_type == "newly_ranked_keywords":
                record = keywords_processor.process_newly_ranked(
                    origin=url,
                    domain=domain,
                    country=country,
                    run_id=run_id,
                )
            elif process_type == "top_ads":
                record = ads_processor.process(
                    origin=url,
                    domain=domain,
                    country=country,
                    run_id=run_id,
                )
            elif process_type == "domain_stats":
                record = domain_stats_processor.process(
                    origin=url,
                    domain=domain,
                    country=country,
                    run_id=run_id,
                )
            else:
                raise RuntimeError("Unexpected process_type dispatch error.")

            records.append(record)
        except Exception as exc:  # noqa: BLE001
            LOGGER.exception("Failed to process %s: %s", url, exc)

    return records

def run_bulk(
    input_file: str,
    country: Optional[str],
    process_type: str,
    output_format: str,
    output_path: str,
    settings_path: Optional[str],
    log_config_path: str,
) -> List[Dict[str, Any]]:
    configure_logging(log_config_path)
    LOGGER.info("Starting SpyFu bulk run")
    LOGGER.info(
        "Params: input_file=%s country=%s process_type=%s output_format=%s output_path=%s",
        input_file,
        country,
        process_type,
        output_format,
        output_path,
    )

    settings = load_settings(settings_path)
    urls = read_urls_from_file(input_file)
    records = process_urls(urls, country, process_type, settings)

    if not records:
        LOGGER.warning("No records generated for this run.")
        return []

    validate_records(records)
    export_records(records, output_path, output_format)
    LOGGER.info("Run complete. Exported %d records to %s", len(records), output_path)
    return records

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="SpyFu (Bulk URLs) scraper CLI",
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input_file",
        default="data/input_urls.sample.txt",
        help="Path to input file containing website URLs (one per line).",
    )
    parser.add_argument(
        "-c",
        "--country",
        dest="country",
        default=None,
        help="Target country code (e.g. US, UK, DE).",
    )
    parser.add_argument(
        "-p",
        "--process",
        dest="process_type",
        required=True,
        choices=[
            "top_competitors",
            "most_valuable_keywords",
            "newly_ranked_keywords",
            "top_ads",
            "domain_stats",
        ],
        help="Type of SpyFu-based process to run.",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_path",
        default="data/output.json",
        help="Path where results will be written (JSON or CSV).",
    )
    parser.add_argument(
        "-f",
        "--format",
        dest="output_format",
        choices=["json", "csv"],
        default="json",
        help="Output format.",
    )
    parser.add_argument(
        "--settings",
        dest="settings_path",
        default="src/config/settings.example.json",
        help="Path to JSON settings file.",
    )
    parser.add_argument(
        "--log-config",
        dest="log_config_path",
        default="src/config/logging.conf",
        help="Path to logging configuration file.",
    )
    return parser

def main_from_cli(argv: Optional[List[str]] = None) -> None:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    run_bulk(
        input_file=args.input_file,
        country=args.country,
        process_type=args.process_type,
        output_format=args.output_format,
        output_path=args.output_path,
        settings_path=args.settings_path,
        log_config_path=args.log_config_path,
    )

if __name__ == "__main__":
    main_from_cli()