from pydantic import BaseModel
from typing import Optional

class ReceiptResponse(BaseModel):
    transaction_id: Optional[str]
    amount: Optional[str]
    date: Optional[str]
    suspicious_metadata: bool
    raw_text: str
    ela_heatmap_path: Optional[str] = None