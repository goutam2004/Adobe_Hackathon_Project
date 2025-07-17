import json
import os

def save_json(title, headings, output_path):
    data = {
        "title": title,
        "outline": headings
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
