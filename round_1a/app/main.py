import os
from extractor import extract_headings
from formatter import save_json

def main():
    input_dir = os.path.join(os.path.dirname(__file__), "input")
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.endswith(".pdf"):
            continue
        pdf_path = os.path.join(input_dir, filename)
        title, headings = extract_headings(pdf_path)
        output_filename = os.path.splitext(filename)[0] + ".json"
        output_path = os.path.join(output_dir, output_filename)
        save_json(title, headings, output_path)
        print(f"[✓] Extracted: {output_filename}")

if __name__ == "__main__":
    main()
