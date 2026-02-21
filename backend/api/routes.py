from fastapi import APIRouter, UploadFile, File
import shutil
import os

from ocr.extractor import extract_text
from forensics.metadata import extract_metadata, check_editing_software
from schemas.receipt import ReceiptResponse
from forensics.ela import perform_ela
router = APIRouter()

UPLOAD_DIR = "temp_uploads"
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

        # ELA heatmap
        ela_image = perform_ela(file_path)
        ela_path = os.path.join(UPLOAD_DIR, f"ELA_{file.filename}")
        ela_image.save(ela_path)

        return {
            "transaction_id": ocr_data["transaction_id"],
            "amount": ocr_data["amount"],
            "date": ocr_data["date"],
            "suspicious_metadata": suspicious,
            "raw_text": ocr_data["raw_text"],
            "ela_heatmap_path": ela_path
        }

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}