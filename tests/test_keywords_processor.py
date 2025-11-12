from src.processors.keywords_processor import KeywordsProcessor
from src.services.spyfu_client import SpyfuClient
from src.outputs.schema_validator import validate_records

def test_keywords_processor_most_valuable() -> None:
    client = SpyfuClient(base_url="https://example.com", use_sample_data=True)
    processor = KeywordsProcessor(client)

    record = processor.process_most_valuable(
        origin="https://example.com",
        domain="example.com",
        country="US",
        run_id="test-run",
    )

    validate_records([record])

    assert record["process_type"] == "most_valuable_keywords"
    assert record["most_valuable_keywords"]
    assert record["most_successful_keywords"]

def test_keywords_processor_newly_ranked() -> None:
    client = SpyfuClient(base_url="https://example.com", use_sample_data=True)
    processor = KeywordsProcessor(client)

    record = processor.process_newly_ranked(
        origin="https://example.com",
        domain="example.com",
        country="US",
        run_id="test-run",
    )

    validate_records([record])

    assert record["process_type"] == "newly_ranked_keywords"
    assert record["newly_ranked_keywords"]