from typing import Any


def calculate_fraud_score(
    validation_result: dict[str, Any],
    suspicious_metadata: bool,
    ocr_data: dict[str, Any],
) -> dict[str, Any]:
    score = 100
    penalties: list[str] = []

    if suspicious_metadata:
        score -= 35
        penalties.append("Suspicious editing software found in metadata (-35)")

    if not validation_result.get("is_supported_bank", True):
        score -= 20
        penalties.append("Unsupported bank flow for current ruleset (-20)")

    if not validation_result.get("transaction_id_valid", False):
        score -= 20
        penalties.append("Transaction ID invalid or missing (-20)")

    if not validation_result.get("amount_valid", False):
        score -= 15
        penalties.append("Amount invalid or missing (-15)")

    if not validation_result.get("date_valid", False):
        score -= 15
        penalties.append("Date invalid, missing, or logically inconsistent (-15)")

    missing_core = sum(
        1
        for field in ("transaction_id", "amount", "date")
        if not ocr_data.get(field)
    )
    if missing_core == 3:
        score -= 20
        penalties.append("OCR failed to extract all core fields (-20)")

    score = max(0, min(100, score))

    if score >= 75:
        risk_level = "low"
    elif score >= 45:
        risk_level = "medium"
    else:
        risk_level = "high"

    return {
        "trust_score": score,
        "risk_level": risk_level,
        "penalties": penalties,
    }
