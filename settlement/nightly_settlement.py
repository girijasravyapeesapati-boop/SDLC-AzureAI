from .settlement_repository import fetch_pending_batches, mark_batch_failed, mark_batch_success
from .notification_service import notify_error
import time

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 10  # exponential backoff baseline

def process_batch(batch):
    """
    Actual settlement batch processor.
    Returns True on success, False on failure.
    """
    # Simulated logic -- replace with real external API calls/moves.
    if batch.get('should_fail', False):  # inject failure for test/demo
        return False
    return True

def run_nightly_settlement():
    batches = fetch_pending_batches()
    for batch in batches:
        success = False
        for attempt in range(1, MAX_RETRIES + 1):
            success = process_batch(batch)
            if success:
                mark_batch_success(batch['id'])
                break
            else:
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY_SECONDS * attempt)  # exponential backoff
        if not success:
            mark_batch_failed(batch['id'])
            notify_error(f"Settlement batch {batch['id']} failed after {MAX_RETRIES} attempts.")
