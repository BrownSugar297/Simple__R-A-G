import signal
import sys
from google import genai
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

GEMINI_API_KEY = "AIzaSyDpoCh29VLO4ybFeM7PH6LzuCqY2khFyao"

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vector_db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

def signal_handler(sig, frame):
    print("\nThanks for using Gemini.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def generate_answer(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

print(generate_answer("\n\n Introduce yourself briefly"))

while True:
    print("\n-------------------------------------")
    query = input("Query: ")

    docs = vector_db.similarity_search(query, k=4)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    answer = generate_answer(prompt)
    print("\nAnswer:", answer)