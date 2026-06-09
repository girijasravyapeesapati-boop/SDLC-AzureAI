# Merchant KYC Integration MVP

Assumptions:
- KYC API uses a mock endpoint https://api.acmekyc.com/kyc/verify
- Returns JSON: { "status": "approved" | "rejected" }
- No persistent DB, uses in-memory list
- Real ops alerts are stubbed as print()

## Usage
- Run `pip install -r requirements.txt`
- Start the Flask server: `python app.py`
- Signup via POST /signup with JSON: { name, email, business_info }
