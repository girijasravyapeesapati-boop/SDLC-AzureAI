import requests
from models import KYCResult

def submit_kyc(merchant):
    try:
        response = requests.post(
            "https://api.acmekyc.com/kyc/verify",
            json={"name": merchant.name, "email": merchant.email, "business_info": merchant.business_info},
            timeout=5,
        )
        if response.status_code == 200:
            status = response.json().get("status")
            if status in ["approved", "rejected"]:
                return KYCResult(status)
        return KYCResult("error")
    except Exception:
        return KYCResult("error")
