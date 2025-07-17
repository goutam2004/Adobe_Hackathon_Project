import fitz  # PyMuPDF
import re
import os
from collections import Counter

def extract_headings(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    headings = []
    font_sizes = []

    # 1) First pass: collect all font sizes across document
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line.get("spans", []):
                    font_sizes.append(round(span["size"], 1))

    # Determine the top 3 most common sizes
    size_counts = Counter(font_sizes)
    common_sizes = [size for size, _ in size_counts.most_common(3)]

    def classify(size):
        if size == common_sizes[0]:
            return "H1"
        elif len(common_sizes) > 1 and size == common_sizes[1]:
            return "H2"
        elif len(common_sizes) > 2 and size == common_sizes[2]:
            return "H3"
        return None

    # 2) Second pass: extract headings based on relative sizes
    for page_num, page in enumerate(doc, start=1):
        height = page.rect.height
        for block in page.get_text("dict")["blocks"]:
            # Skip non-text or footers near bottom (last 50 pts)
            if "lines" not in block or block["bbox"][1] > height - 50:
                continue

            for line in block["lines"]:
                spans = line.get("spans", [])
                if not spans:
                    continue

                text = "".join(span["text"] for span in spans).strip()
                if len(text) < 3:
                    continue

                size = round(spans[0]["size"], 1)
                level = classify(size)
                if not level:
                    continue

                clean_text = re.sub(r"\s+", " ", text)
                headings.append({
                    "level": level,
                    "text": clean_text,
                    "page": page_num
                })

    # 3) Title extraction: metadata → first H1 on page 1 → filename
    title = doc.metadata.get("title", "").strip()
    if not title:
        for h in headings:
            if h["level"] == "H1" and h["page"] == 1:
                title = h["text"]
                break
    if not title:
        title = os.path.basename(pdf_path).replace(".pdf", "")

    return title, headings
