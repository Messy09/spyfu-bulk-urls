# API Reference

## CLI

Module: `src.cli`

### `main(argv: Optional[List[str]] = None) -> None`

Entry point for the command-line interface. Delegates to `src.runner.main_from_cli`.

## Runner

Module: `src.runner`

### `run_bulk(input_file, country, process_type, output_format, output_path, settings_path, log_config_path)`

High-level orchestration for:

1. Configuring logging.
2. Loading settings.
3. Reading URLs from file.
4. Dispatching to the appropriate processor.
5. Validating records.
6. Exporting JSON or CSV output.

## Services

### `SpyfuClient`

Module: `src.services.spyfu_client`

Methods:

- `get_top_competitors(domain, country)`
- `get_most_valuable_keywords(domain, country)`
- `get_newly_ranked_keywords(domain, country)`
- `get_top_ads(domain, country)`
- `get_domain_stats(domain, country)`

When `use_sample_data` is enabled, methods return synthetic but structured data.

### `ProxyManager`

Module: `src.services.proxy_manager`

Round-robin rotation over configured proxy URLs.

### `RequestThrottler`

Module: `src.services.request_throttler`

Simple rate limiter based on requests per minute.

## Processors

- `CompetitorsProcessor` (`src.processors.competitors_processor`)
- `KeywordsProcessor` (`src.processors.keywords_processor`)
- `AdsProcessor` (`src.processors.ads_processor`)
- `DomainStatsProcessor` (`src.processors.domain_stats_processor`)

Each exposes a `process(...)` method that returns a normalized record.

## Outputs

### `export_records(records, output_path, fmt)`

Module: `src.outputs.exporters`  
Exports to JSON (`fmt="json"`) or CSV (`fmt="csv"`).

### `validate_records(records)`

Module: `src.outputs.schema_validator`  
Validates records against the documented schema using `jsonschema`.