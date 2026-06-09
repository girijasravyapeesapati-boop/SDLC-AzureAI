import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_kyc_approved(monkeypatch, client):
    from kyc_client import submit_kyc
    monkeypatch.setattr('kyc_client.submit_kyc', lambda m: type("R", (), {"status": "approved"})())
    res = client.post("/signup", json={"name": "Test1", "email": "a@b.com", "business_info": "LLC"})
    assert res.status_code == 200 and res.json["status"] == "approved"

def test_kyc_rejected(monkeypatch, client):
    monkeypatch.setattr('kyc_client.submit_kyc', lambda m: type("R", (), {"status": "rejected"})())
    res = client.post("/signup", json={"name": "Test2", "email": "c@d.com", "business_info": "Sole Trader"})
    assert res.status_code == 400 and res.json["status"] == "rejected"

def test_kyc_error(monkeypatch, client):
    monkeypatch.setattr('kyc_client.submit_kyc', lambda m: type("R", (), {"status": "error"})())
    res = client.post("/signup", json={"name": "Err", "email": "fail@ops.com", "business_info": "Inc"})
    assert res.status_code == 202 and res.json["status"] == "manual_review"
