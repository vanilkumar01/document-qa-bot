import os
from dotenv import load_dotenv
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

def ask_question(user_query: str, db_path: str = "./db", k: int = 3):
    try:
        client = chromadb.PersistentClient(path=db_path)

        embedding_fn = (
            embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
        )

        collection = client.get_collection(
            name="document_knowledge_base",
            embedding_function=embedding_fn
        )

        results = collection.query(
            query_texts=[user_query],
            n_results=k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context_parts = []

        for doc, meta in zip(documents, metadatas):
            source = meta.get("source", "Unknown")
            page = meta.get("page", "N/A")
            context_parts.append(
                f"Source: {source}, Page: {page}\n{doc}"
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You are a helpful document assistant.

Answer ONLY from the context below.

If the answer is not available in the context, say:
'I could not find the answer in the provided documents.'

Context:
{context}

Question:
{user_query}

Answer:
"""

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

