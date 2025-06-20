
 📄 PDF to Structured MCQ Pipeline

This project provides an automated pipeline to extract **multiple-choice questions (MCQs)** from PDF files using OCR and NLP. It processes PDF files by:

1. Converting PDFs to images.
2. Performing OCR on those images.
3. Analyzing the extracted text to produce a structured JSON format.



 🧠 Key Features

* Converts PDF pages to images (`moamolpdf`)
* Extracts text from images using **Google Vision OCR** (`MoamalOCR`)
* Parses the text to generate clean MCQ data (`process_txt_files`)
* Saves final output as a JSON file

---

📁 Project Structure

```
.
├── model.py                          # Main pipeline logic
├── moamolpdf/                        # PDF to image conversion module
├── moamalocr/                        # OCR module using Google Vision
├── moamalnpl/                        # NLP processing for MCQs
├── credentials.json                  # Google Vision API credentials
├── images/                           # Stores images generated from PDFs
├── outputtext/                       # Raw text output from OCR
├── static/structured_output/        # Final structured JSON output
```

## 🛠️ Requirements

Make sure you have Python 3.8+ installed. Install the necessary packages:

```bash
pip install google-cloud-vision pillow tqdm
```

Also, make sure to:

* Enable the **Google Cloud Vision API**.
* Provide a valid `credentials.json` file for authentication.


🚀 How to Run

Call the `run_pipeline()` function in `model.py` with a PDF file path:

python
from model import run_pipeline

run_pipeline("path/to/your_file.pdf")


This will:

* Create folders: `images/`, `outputtext/`, and `static/structured_output/`
* Generate: `your_file.json` inside `static/structured_output/`



 📤 Output Format

The final output is a JSON file with MCQs structured like this:

```json
[
  {
    "question": "What is the capital of France?",
    "options": ["London", "Paris", "Rome", "Berlin"],
    "answer": "Paris",
    "explanation": "Paris is the capital of France."
  },
  ...
]
```

---

 🔐 Credentials

Make sure to add your `credentials.json` (Google Cloud Vision API) in the root directory.

---

✅ Use Cases

* Educational platforms converting paper exams to digital MCQs
* Data extraction for training AI models on structured Q\&A
* Automating digitization of academic content

---

## 📄 License

This project is for educational and experimental use. Feel free to contribute or adapt it for your own needs.


