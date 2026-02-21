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
async def verify_receipt(file: UploadFile= File()):
    try :
        # save uploaded file to temp directory
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # extract metadata
        metadata = extract_metadata(file_path)
        # check for editing software
        suspicious = check_editing_software(metadata)
        # perform OCR
        ocr_result = extract_text(file_path)
        # perform ELA analysis
        ela_image = perform_ela(file_path)
        ela_path = os.path.join(UPLOAD_DIR, f"ela_{file.filename}")
        ela_image.save(ela_path)
        
        return ReceiptResponse(
            filename=file.filename,
            metadata=metadata,
            suspicious=suspicious,
            ocr_result=ocr_result,
            ela_path=ela_path
        )
    except Exception as e:
        print("Error: ", e)
        return {"error": str(e)}