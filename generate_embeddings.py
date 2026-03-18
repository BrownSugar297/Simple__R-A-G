from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("./report.pdf")
docs = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

docs = text_splitter.split_documents(docs)

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
vectorstore = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="./chroma_db"
)

print("Stored documents:", vectorstore._collection.count())