### Ethio-verify

*"The OCR read the amount correctly, but the Error Level Analysis (ELA) showed a high noise variance in the 'Amount' field, suggesting it was modified. Therefore, even though the Transaction ID exists in my DB, the system flagged it as 'Tampered'."*

Layer       Technology      Why?
Language    Python 3.10+    The undisputed king of image processing and OCR.
API Framework       FastAPI       Extremely fast, handles asynchronous uploads, and auto-generates your documentation (Swagger)
Image Forensics       OpenCV + Pillow       Essential for ELA (Error Level Analysis) and pixel manipulation.
Text Extraction       PaddleOCR or EasyOCR       Better than Tesseract for receipts; they handle tilted or blurry text much more accurately.
Frontend       Next.js (React)       "To build a clean ""Security Dashboard"" that shows the forensic heatmaps."
Database       PostgreSQL       "To store the ""Source of Truth"" transaction records for Pathway 4."

## 🗺️ Build Roadmap: The 4-Phase Sprint

# Phase 1: The "Entry & Extraction" (Week 1)

Goal: Get the image into the system and read the data.

- Setup: Create a FastAPI project structure.

- Pathway 1: Write a utility using Pillow to extract EXIF metadata. Flag anything containing "Adobe," "Canva," or "Editor."

- Pathway 3 (Part A): Integrate EasyOCR. Extract the Transaction_ID, Amount, and Date.

- Validation: Write regex patterns to ensure the Transaction ID follows the expected format (e.g., TXN-12345-ABC).

# Phase 2: The "Digital Forensics" (Week 2)

Goal: Detect the invisible edits.

- Pathway 2 (ELA): Implement the Error Level Analysis logic. You basically resave the image at 95% quality and calculate the "pixel difference" between the two versions.

- Pathway 2 (Texture): Use OpenCV to detect "blurs" around the text. Edited text usually has smoother edges than the rest of the screenshot.

- Visualization: Save these forensic "heatmaps" as temporary files to show the user later.

# Phase 3: The "Source of Truth" (Week 3)
Goal: Verify if the transaction actually exists.

- Database Setup: Create a SQL table with dummy data (Mock Transactions).

- Pathway 4: Create a "Verification Service" that takes the OCR data and queries your DB.

- Pathway 3 (Part B): Implement "Logical Checks." (e.g., If the date extracted is in the future, auto-fail it).

# Phase 4: The "Scoring Engine" & UI (Week 4)
Goal: Bring it all together.

- The Engine: Write the final function that collects results from all 4 pathways and calculates the weighted score.

- The Dashboard: Build a React frontend where a user uploads a screenshot and sees:
    * The Original Image.
    * The ELA Heatmap (glowing areas = suspicious).
    * A "Security Report" showing which pathway passed or failed.

# 📁 Suggested Repository Structure

/receipt-verifier
├── /backend
│   ├── /api          # FastAPI routes
│   ├── /forensics    # ELA and metadata logic
│   ├── /ocr          # Text extraction and regex logic
│   ├── /db           # Database models and mock data
│   └── main.py       # Entry point
├── /frontend
│   ├── /components   # File upload and result cards
│   └── /pages        # Main dashboard
└── requirements.txt what do you think about htis 