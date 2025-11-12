from src.processors.competitors_processor import CompetitorsProcessor
from src.services.spyfu_client import SpyfuClient
from src.outputs.schema_validator import validate_records

def test_competitors_processor_builds_valid_record() -> None:
    client = SpyfuClient(base_url="https://example.com", use_sample_data=True)
    processor = CompetitorsProcessor(client)

    record = processor.process(
        origin="https://example.com",
        domain="example.com",
        country="US",
        run_id="test-run",
    )

    validate_records([record])

    assert record["domain"] == "example.com"
    assert record["process_type"] == "top_competitors"
    assert isinstance(record["top_competitors"], list)
    assert record["top_competitors"], "Expected at least one competitor."