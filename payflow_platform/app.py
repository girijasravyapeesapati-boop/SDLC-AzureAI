from flask import Flask, request, jsonify
from models import Merchant
from kyc_client import submit_kyc
from manual_review import notify_ops

app = Flask(__name__)
MERCHANTS = []

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    merchant = Merchant(data['name'], data['email'], data['business_info'])
    kyc_result = submit_kyc(merchant)
    if kyc_result.status == "approved":
        merchant.status = "active"
        MERCHANTS.append(merchant)
        return jsonify({"message": "Merchant onboarded", "status": "approved"}), 200
    elif kyc_result.status == "rejected":
        merchant.status = "rejected"
        return jsonify({"message": "Merchant rejected by KYC", "status": "rejected"}), 400
    else:
        merchant.status = "manual_review"
        notify_ops(merchant)
        return jsonify({"message": "KYC error, manual review required", "status": "manual_review"}), 202

if __name__ == "__main__":
    app.run()
