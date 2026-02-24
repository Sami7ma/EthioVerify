from pydantic import BaseModel
from typing import Optional

class ReceiptResponse(BaseModel):
    transaction_id: str | None
    amount: str | None
    date: str | None

    ocr_confidence: float      # 👈 ADD
    suspicious_metadata: bool
    raw_text: str

    ela_heatmap_path: str
    ela_score: float           # 👈 ADD

    bank_detected: str | None
    risk_flags: list[str]
    rule_score: int

    final_score: float
    classification: str