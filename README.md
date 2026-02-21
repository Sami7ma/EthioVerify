# Ethio-Verify 🔐

Ethio-Verify is a forensic verification system designed to detect tampered Ethiopian bank payment screenshots using OCR, metadata analysis, and digital image forensics.

This project demonstrates backend engineering, image processing, and fraud detection techniques.

---

## 🚀 Current Capabilities (Phase 1 + Phase 2)

- 📸 Image upload via FastAPI
- 🔍 EXIF metadata extraction
- ⚠ Detection of suspicious editing software (Adobe, Canva, etc.)
- 🧠 OCR-based text extraction (Transaction ID, Amount, Date)
- 🧾 Regex validation of extracted fields
- 📊 Structured JSON response

---

## 🧱 Tech Stack

| Layer            | Technology         | Purpose                     |
| ---------------- | ------------------ | --------------------------- |
| Backend          | FastAPI            | API framework               |
| OCR              | EasyOCR            | Text extraction             |
| Image Processing | Pillow             | Metadata + image operations |
| Forensics        | OpenCV + PIL       | Error Level Analysis        |
| Validation       | Regex + Rule Logic | Field verification          |


---

## 📁 Project Structure

```
/receipt-verifier
├── /backend
│   ├── /api
│   ├── /forensics
│   ├── /ocr
│   ├── /schemas
│   ├── /services
│   └── main.py
└── requirements.txt
```

---

## 📊 Architecture Diagram
User Upload
    ↓
FastAPI Endpoint
    ↓
Preprocessing Layer
    ├── Metadata Analyzer
    ├── OCR Engine
    └── ELA Engine
    ↓
Extraction Normalizer
    ↓
Rule Engine (Phase 3)
    ↓
Scoring Engine (Phase 4)
    ↓
Fraud Report Builder
    ↓
Structured JSON Response


## ⚙ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ethio-verify.git
cd receipt-verifier/backend
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pillow easyocr python-multipart
pip install opencv-python numpy
```

### 3️⃣ Run Server

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Sample API Response

```json
{
  "transaction_id": "FT26O28DSHZW",
  "amount": "ETB 3,000.00",
  "date": "28-Jan-2026",
  "suspicious_metadata": false,
  "ela_heatmap_path": "temp_uploads/ELA_image.jpg",
  "raw_text": "..."
}
```

---
## 🔬 Roadmap

### Phase 3 – Source of Truth Verification
This phase introduces rule-based fraud detection logic.

OCR + ELA alone are not sufficrnt.
Logical validation strengthens verification relaiability.
We are gonna use bank detection from ocr text

**Logical Validation Rules**
- ❌ Future transaction Date -> Auto-Fail 
- ❌ Amount ≤ 0 -> Invalid
- ❌ Transaction ID format mismatch by detecting each banks txn format → Suspicious
- ❌ Screesnhot date vs transaction date consistency → Suspicious
- ❌ Transaction ID format mismatch → Suspicious
- ❌ Missing required fields → High Risk

### 🏁 Phase 4 – Fraud Scoring Engine
Instead of binary pass/Fail descions, Ethio-verify calculates a weighted fraud confidence score:

Final Score =
  (Metadata Score * 0.15) +
  (ELA Score * 0.35) +
  (OCR Confidence * 0.15) +
  (Rule Validation Score * 0.35)

**Score Classification** will be something like:

| Score Range | Result     |
| ----------- | ---------- |
| 0 – 40      | Tampered   |
| 41 – 70     | Suspicious |
| 71 – 100    | Verified   |

.

*🔬 Future Enhancements*

- Blur & texture inconsistency detection
- Base64 heatmap return for frontend dashboards
- Next.js forensic dashboard
- Multi-bank parser modules
- Docker containerization

---

## 🎯 Purpose

This project is built as a portfolio demonstration of:

- Backend API design
- Digital image forensics analysis
- OCR integration
- Rule-based Fraud detection logic
- Clean, modular system architecture

---

## 👨‍💻 Author

Samuel  
Computer Science and Software Engineering Student
Focused on Backend Systems, Computer Vision & Secure Application Design.
