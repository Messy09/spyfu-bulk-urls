from src.processors.domain_stats_processor import DomainStatsProcessor
from src.services.spyfu_client import SpyfuClient
from src.outputs.schema_validator import validate_records

def test_domain_stats_processor() -> None:
    client = SpyfuClient(base_url="https://example.com", use_sample_data=True)
    processor = DomainStatsProcessor(client)

    record = processor.process(
        origin="https://example.com",
        domain="example.com",
        country="US",
        run_id="test-run",
    )

    validate_records([record])

    assert record["process_type"] == "domain_stats"
    stats = record["domain_stats"]
    assert isinstance(stats, dict)
    assert "estimated_monthly_clicks" in stats
    assert stats["estimated_monthly_clicks"] > 0