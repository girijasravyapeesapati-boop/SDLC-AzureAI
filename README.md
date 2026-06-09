# Nightly Settlement Retry Automation

This module automates nightly settlement batch processing with built-in retry, error flagging, and notification logic.

**Key Features:**
- Batch retry up to N times with exponential backoff
- Marks failed batches and alerts on ultimate failure
- Fully testable with pytest

**How to Run**
1. Schedule `run_nightly_settlement()` daily (crontab, Airflow, etc.)
2. Configure MAX_RETRIES and RETRY_DELAY_SECONDS as per ops policy

**Testing**
Run:
```bash
pytest tests/test_nightly_settlement.py
```
