import pytest
from settlement import nightly_settlement
from settlement import settlement_repository

def setup_function():
    # Reset repository before each test if needed
    settlement_repository._failed.clear()
    settlement_repository._success.clear()

def test_successful_batch_settlement(monkeypatch):
    monkeypatch.setattr(nightly_settlement, "process_batch", lambda batch: True)
    nightly_settlement.run_nightly_settlement()
    assert 1 in settlement_repository.get_successful_batches()

def test_failed_batch_settlement(monkeypatch):
    monkeypatch.setattr(nightly_settlement, "process_batch", lambda batch: False)
    nightly_settlement.run_nightly_settlement()
    assert 1 in settlement_repository.get_failed_batches() or 2 in settlement_repository.get_failed_batches()

def test_retry_logic(monkeypatch):
    # Fail twice, then succeed
    call_counter = {"count": 0}
    def flaky_process(batch):
        call_counter["count"] += 1
        return call_counter["count"] >= 3
    monkeypatch.setattr(nightly_settlement, "process_batch", flaky_process)
    nightly_settlement.run_nightly_settlement()
    assert 1 in settlement_repository.get_successful_batches()
