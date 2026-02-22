from datetime import datetime
from validators.bank_patterns import detect_bank, validate_transaction_id

def validate_receipt_logic(data: dict):
    risk_flags = []
    rule_score = 100

    # 1. missing critical fields

    required_fields = ["transaction_id", "amount", "date"]

    for field in required_fields:
        if not data.get(field):
            risk_flags.append(f"Missing {field}")
            rule_score -= 30
    
    # 2️. Future Date
    try:
        receipt_date = datetime.strptime(data["date"], "%d-%b-%Y")
        if receipt_date > datetime.now():
            risk_flags.append("Future transaction date")
            rule_score -= 50
    except:
        risk_flags.append("Invalid date format")
        rule_score -= 20
    
    # 3. Amount validation
    try:
        amount_numeric = float(data["amount"].replace("ETB","")).replace(",","").strip()
        if amount_numeric <= 0:
            risk_flags.append("Non-positive amount")
            rule_score -= 30
    except:
        risk_flags.append("Invalid amount format")
        rule_score -= 20
    
    #4. Bank + Transaction ID consistency
    bank = detect_bank(data["raw_text"])
    txn_id = validate_transaction_id(data["transaction_id"], bank)
    if not txn_id:
        risk_flags.append(f"Transaction ID does not match {bank} pattern")
        rule_score -= 30
    
    return{
        "bank_detected": bank,
        "risk_flags": risk_flags,
        "rule_score": max(rule_score, 0)
    }