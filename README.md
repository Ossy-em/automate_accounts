# Receipt Processing API

This Django-based project allows users to upload receipts (PDFs), validate them, and extract structured data using OCR.

---

##  Requirements

- Python 3.10+
- pip
- Tesseract OCR
- Poppler for PDF rendering
- asgiref==3.8.1
- Django==5.2.2
- djangorestframework==3.16.0
- packaging==25.0
- pdf2image==1.17.0
- pillow==11.2.1
- pytesseract==0.3.13
- python-dateutil==2.9.0.post0
- six==1.17.0
sqlparse==0.5.3


---

## Setup Instructions

1. Clone the project or unzip it:

```bash
unzip automate_accounts.zip
cd automate_accounts

2. Install dependencies:
pip install -r requirements.txt

3. Setup OCR dependencies:
brew install tesseract poppler (macOS)

4. Run migration:
python manage.py migrate

5. Start the server:
python manage.py runserver


** ## API Usage** (POSTMAN TEST)
 Upload Receipt
POST /api/upload/
Validate Receipt
POST /api/validate/
 Process Receipt
POST /api/process/
List Receipts
GET /api/receipts/
Receipt Detail
GET /api/receipts/<id>/

