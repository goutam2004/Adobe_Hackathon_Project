from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_path, persona_query):
    doc = fitz.open(pdf_path)
    paragraphs = []

    for page in doc:
        blocks = page.get_text("blocks")
        for b in blocks:
            text = b[4].strip()
            if len(text) > 30:
                paragraphs.append(text)
    doc.close()

    if not paragraphs:
        return ""

    return get_most_relevant_paragraphs(persona_query, paragraphs)

def get_most_relevant_paragraphs(query, paragraphs, top_k=5):
    query_vec = model.encode([query])[0]
    para_vecs = model.encode(paragraphs)

    sims = cosine_similarity([query_vec], para_vecs)[0]
    ranked = sorted(zip(sims, paragraphs), reverse=True)[:top_k]

    return " ".join([para for _, para in ranked])
