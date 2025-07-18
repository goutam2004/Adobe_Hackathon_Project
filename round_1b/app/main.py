import os
import json
from processor import process_collection

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def main():
    config = load_json("app/config.json")
    personas = load_json("app/personas.json")

    input_root = config["collections_path"]
    output_root = config["output_path"]

    for collection_name in os.listdir(input_root):
        collection_path = os.path.join(input_root, collection_name)
        if not os.path.isdir(collection_path):
            continue

        for persona_data in personas:
            persona = persona_data["persona"]
            job = persona_data["job_to_be_done"]
            tag = persona.lower().replace(" ", "_")

            print(f"🔍 Processing {collection_name} for persona '{persona}'...")

            result = process_collection(collection_path, persona, job)

            output_filename = f"{collection_name}_{tag}_result.json"
            output_path = os.path.join(output_root, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    main()
