import os
import chromadb
from pypdf import PdfReader
from chromadb.utils import embedding_functions

def extract_pdf_pages(file_path: str):
    extracted_data = []
    file_name = os.path.basename(file_path)

    try:
        reader = PdfReader(file_path)

        for index, page in enumerate(reader.pages):
            text = page.extract_text()

            if text and text.strip():
                clean_text = " ".join(text.split())

                extracted_data.append({
                    "text": clean_text,
                    "metadata": {
                        "source": file_name,
                        "page": index + 1
                    }
                })

    except Exception as e:
        print(f"Error reading PDF {file_name}: {e}")

    return extracted_data

def chunk_extracted_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=200
):
    chunks = []

    for page in pages:
        text = page["text"]
        metadata = page["metadata"]

        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))

            chunks.append({
                "text": text[start:end],
                "metadata": {
                    "source": metadata["source"],
                    "page": metadata["page"]
                }
            })

            start += (chunk_size - chunk_overlap)

    return chunks


def save_to_vector_db(chunks, db_path="./db"):
    client = chromadb.PersistentClient(path=db_path)

    embedding_fn = (
        embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
    )

    collection = client.get_or_create_collection(
    name="document_knowledge_base",
    embedding_function=embedding_fn
)

    ids = [f"id_{i}" for i in range(len(chunks))]
    documents = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    print(
        f"Successfully indexed {len(chunks)} chunks."
    )
