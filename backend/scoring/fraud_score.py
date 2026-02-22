from core.config import Settings

def compute_fraud_score(metadata_flag: bool,
                        ela_score: float,
                        ocr_confidence: float,
                        rule_score: float):
    
    metadata_score = 0 if metadata_flag else 100

    final_score = (
        metadata_score * Settings.METADATA_WEIGHT +
        ela_score * Settings.ELA_WEIGHT +
        ocr_confidence * Settings.OCR_WEIGHT +
        rule_score * Settings.RULES_WEIGHT
    )
    return round(final_score, 2)

def classify_score(score):
    if score <= 40:
        return "Tampered"
    elif score <= 70:
        return "Suspicious"
    else:
        return "Verified"