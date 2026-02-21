def compute_fraud_score(metadata_flag: bool, ela_score: float, ocr_confidence: float, rule_score: float)-> int:
    metadata_score = 0 if metadata_flag else 100

    final_score = (
        metadata_score * 0.15 +
        ela_score * 0.35 +
        ocr_confidence * 0.15 +
        rule_score * 0.35
    )
    return round(final_score, 2)

def classify_score(score):
    if score <= 40:
        return "Tampered"
    elif score <= 70:
        return "Suspicious"
    else:
        return "Verified"