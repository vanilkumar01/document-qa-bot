# 📚 Document Q&A Bot

A Retrieval-Augmented Generation (RAG) application that enables users to ask questions about uploaded documents and receive context-aware answers using semantic search and Google Gemini.

## Features

* PDF and DOCX document ingestion
* Automatic text extraction and preprocessing
* Intelligent text chunking with overlap
* ChromaDB vector database storage
* Semantic similarity search
* Context-aware answer generation using Gemini
* Streamlit-based user interface

## Tech Stack

* Python
* Streamlit
* ChromaDB
* Google Gemini
* PyPDF
* Python-Docx

## Project Structure

```text
document-qa-bot/
├── data/
│   ├── business_doc.pdf
│   ├── science_paper.pdf
│   └── factsheet.docx
│
├── db/
│
├── src/
│   ├── config.py
│   ├── ingest.py
│   ├── query.py
│   ├── main.py
│   └── __init__.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How It Works

1. Documents are loaded from the data folder.
2. Text is extracted and cleaned.
3. Documents are split into smaller chunks.
4. Chunks are converted into vector embeddings.
5. Embeddings are stored in ChromaDB.
6. User questions are converted into vectors.
7. Similar chunks are retrieved.
8. Retrieved context is sent to Gemini.
9. Gemini generates a grounded answer.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/document-qa-bot.git
cd document-qa-bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Build the Vector Database

```bash
python src/ingest.py
```

## Run the Application

```bash
streamlit run src/main.py
```

## Example Questions

* What is the company's target revenue?
* What are the applications of AI in healthcare?
* Where is TechNova Solutions headquartered?
* Summarize the uploaded documents.
* What services does the company provide?

## RAG Architecture

```text
Documents
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Similarity Search
    ↓
Retrieved Context
    ↓
Google Gemini
    ↓
Answer Generation
```

## Future Enhancements

* Multi-document support
* Source citation highlighting
* Conversational memory
* File upload functionality
* Hybrid search (keyword + semantic search)
* Cloud deployment support

## Author

V Anil Kumar

GitHub: https://github.com/vanilkumar01
LinkedIn: https://www.linkedin.com/in/v-anil-kumar-/
