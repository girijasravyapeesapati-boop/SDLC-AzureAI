class Merchant:
    def __init__(self, name, email, business_info):
        self.name = name
        self.email = email
        self.business_info = business_info
        self.status = "pending"

class KYCResult:
    def __init__(self, status):
        self.status = status  # 'approved', 'rejected', 'error'
