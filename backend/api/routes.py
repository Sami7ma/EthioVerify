from fastapi import APIRouter, UploadFile, File
import shutil
import os

from ocr.extractor import extract_text
from forensics.metadata import extract_metadata, check_editing_software
from schemas.receipt import ReceiptResponse
from forensics.ela import perform_ela
from scoring.fraud_score import compute_fraud_score, classify_score
from validators.rules import validate_receipt_logic
from core.config import settings
router = APIRouter()

UPLOAD_DIR = settings.UPLOAD_DIR
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/verify", response_model=ReceiptResponse)
async def verify_receipt(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Metadata
        metadata = extract_metadata(file_path)
        suspicious = check_editing_software(metadata)

        # OCR
        ocr_data = extract_text(file_path)
        print("OCR DATA:", type(ocr_data))
        # ELA heatmap
        ela_image = perform_ela(file_path)
        ela_path = os.path.join(UPLOAD_DIR, f"ELA_{file.filename}")
        ela_image.save(ela_path)

        #logic validation
        rule_results = validate_receipt_logic(ocr_data)
        print("RULE RESULTS:", type(rule_results))
        ela_score = 85  # Placeholder for ELA score calculation
        ocr_confidence = 90  # Placeholder for OCR confidence score
        final_score = compute_fraud_score(
            metadata_flag=check_editing_software["suspicious_metadata"],
            ela_score=85,
            ocr_confidence=90,  # from EasyOCR if available
            rule_score=rule_results["rule_score"]
        )
        
        classification = classify_score(final_score)

        return {
            "transaction_id": ocr_data["transaction_id"],
            "amount": ocr_data["amount"],
            "date": ocr_data["date"],
            "suspicious_metadata": suspicious,
            "raw_text": ocr_data["raw_text"],
            "ela_heatmap_path": ela_path,

            #phase 3
            "bank_detected": rule_results["bank_detected"],
            "risk_flags": rule_results["risk_flags"],
            "rule_score": rule_results["rule_score"],

            #phase 4

            "final_score": final_score,
            "classification": classification

        }

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(ela_path):
            os.remove(ela_path)