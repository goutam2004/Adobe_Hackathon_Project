import os
from extractor import extract_text_from_pdf

def process_collection(folder_path, persona, job):
    query = f"{persona} {job}"
    output = {
        "persona": persona,
        "job_to_be_done": job,
        "documents": []
    }

    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            summary = extract_text_from_pdf(file_path, query)
            output["documents"].append({
                "document_name": file,
                "summary": summary
            })

    return output
