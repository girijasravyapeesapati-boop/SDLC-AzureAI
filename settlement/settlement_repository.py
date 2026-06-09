_pending_batches = [
    {"id": 1, "should_fail": False},
    {"id": 2, "should_fail": True}
]
_failed = []
_success = []

def fetch_pending_batches():
    # Return a (mocked) copy to process for settlement
    return list(_pending_batches)

def mark_batch_success(batch_id):
    _success.append(batch_id)

def mark_batch_failed(batch_id):
    _failed.append(batch_id)

def get_failed_batches():
    return list(_failed)
def get_successful_batches():
    return list(_success)
