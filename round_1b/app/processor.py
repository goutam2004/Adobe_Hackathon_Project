import os, json
from datetime import datetime
from PyPDF2 import PdfReader

def extract_relevant_sections(doc_path, persona, job):
    reader = PdfReader(doc_path)
    sections = []
    subsections = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        if any(keyword.lower() in text.lower() for keyword in ["methodology", "dataset", "benchmark"]):
            sections.append({
                "document": os.path.basename(doc_path),
                "page": i + 1,
                "section_title": f"Relevant Section from Page {i + 1}",
                "importance_rank": len(sections) + 1
            })
            subsections.append({
                "document": os.path.basename(doc_path),
                "page": i + 1,
                "refined_text": text[:500]
            })
    return sections, subsections

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, "input")
    output_dir = os.path.join(base_dir, "output")
    persona_file = os.path.join(input_dir, "persona.json")

    if not os.path.exists(persona_file):
        raise FileNotFoundError(f"persona.json not found in: {persona_file}")

    with open(persona_file, "r") as f:
        meta = json.load(f)

    all_sections = []
    all_subsections = []

    for pdf in meta["documents"]:
        path = os.path.join(input_dir, pdf)
        if not os.path.isfile(path):
            print(f"[WARN] File not found: {path}")
            continue
        secs, subs = extract_relevant_sections(path, meta["persona"], meta["job"])
        all_sections.extend(secs)
        all_subsections.extend(subs)

    os.makedirs(output_dir, exist_ok=True)

    result = {
        "metadata": {
            "persona": meta["persona"],
            "job": meta["job"],
            "documents": meta["documents"],
            "timestamp": datetime.utcnow().isoformat()
        },
        "sections": all_sections,
        "subsections": all_subsections
    }

    with open(os.path.join(output_dir, "output.json"), "w", encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
