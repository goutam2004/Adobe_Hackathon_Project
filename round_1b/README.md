# 🧾 Round 1B – Adobe Hackathon PDF Outline Extractor

This project extracts relevant sections from multiple PDF collections based on persona and job description.

---

## 📁 Directory Structure

round1_1b/
├── Collection 1/
│ ├── PDFs/
│ ├── persona.json
│ └── collection1_output.json
├── Collection 2/
├── Collection 3/
├── processor.py
├── requirements.txt
└── README.md


---

## 🚀 How to Run

1. **Install dependencies**  
pip install -r requirements.txt


2. **Run the processor**  

3. Outputs will be generated in each `Collection_X/` as `collectionX_output.json`.

---

## 🧠 Logic

- Extracts pages that contain keywords like:  
`"methodology", "dataset", "benchmark"`
- Outputs:
- Relevant sections
- Refined summary (first 500 characters)

---

## 📌 Requirements

- Python 3.8+
- PyPDF2

---

## 📬 Contact

Goutam Dawar – Adobe Hackathon 2025
