import os

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        pass

# Load environment variables
load_dotenv()

# ==========================================
# API Configuration
# ==========================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==========================================
# Directory Paths
# ==========================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
DB_DIR = os.path.join(BASE_DIR, "db")

# ==========================================
# ChromaDB Configuration
# ==========================================
COLLECTION_NAME = "document_knowledge_base"

# ==========================================
# Embedding Configuration
# ==========================================
EMBEDDING_MODEL = "models/text-embedding-004"

# ==========================================
# Text Chunking Configuration
# ==========================================
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ==========================================
# Retrieval Configuration
# ==========================================
TOP_K_RESULTS = 5

# ==========================================
# Gemini LLM Configuration
# ==========================================
LLM_MODEL = "gemini-2.5-flash"

# ==========================================
# Supported File Types
# ==========================================
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt"]