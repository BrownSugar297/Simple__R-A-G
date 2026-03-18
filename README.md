# 📄 Simple RAG — Retrieval-Augmented Generation with PDF

A simple command-line RAG (Retrieval-Augmented Generation) pipeline that lets you chat with any PDF document using local embeddings and Google Gemini as the LLM.

---

## 🗂️ Project Structure

```
.
├── report.pdf                # Your source document
├── generate_embeddings.py    # Chunks the PDF and stores embeddings in ChromaDB
├── rag.py                    # Interactive Q&A loop using Gemini + ChromaDB
└── chroma_db/                # Auto-generated vector store (after running embeddings)
```

---

## ⚙️ How It Works

1. **`generate_embeddings.py`** — Loads the PDF, splits it into chunks, generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`, and persists them to a local ChromaDB vector store.
2. **`rag.py`** — Takes a user query, retrieves the top-4 relevant chunks from ChromaDB, builds a prompt with context, and sends it to Gemini for an answer.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install langchain-chroma langchain-huggingface langchain-community langchain-text-splitters pypdf google-genai
```

### 3. Add your PDF

Place your PDF in the root directory and name it `report.pdf` (or update the path in `generate_embeddings.py`).

### 4. Set your Gemini API key

In `rag.py`, replace the placeholder with your actual key:

```python
GEMINI_API_KEY = "your-api-key-here"
```

> 💡 Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Generate embeddings

```bash
python generate_embeddings.py
```

This creates a `chroma_db/` folder with your document's vector store.

### 6. Start chatting

```bash
python rag.py
```

Type your questions about the document. Press `Ctrl+C` to exit.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `langchain-chroma` | Vector store (ChromaDB) |
| `langchain-huggingface` | HuggingFace embedding model |
| `langchain-community` | PDF loader (`PyPDFLoader`) |
| `langchain-text-splitters` | Chunk the document |
| `pypdf` | PDF parsing backend |
| `google-genai` | Gemini LLM client |

---

## 🧠 Model Details

- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2` (runs locally, no API needed)
- **LLM:** `gemini-2.5-flash` via Google Generative AI API

---

## 📝 Example

```
Query: What was Best Buy's revenue in fiscal 2023?

Answer: Best Buy's total revenue in fiscal year 2023 was $46.3 billion,
representing a 10.6% decline compared to $51.8 billion in fiscal 2022...
```

---

## ⚠️ Notes

- Re-run `generate_embeddings.py` whenever you change the source PDF.
- The `chroma_db/` folder can be deleted to reset the vector store.
- Chunk size and overlap can be tuned in `generate_embeddings.py` (`chunk_size=1000`, `chunk_overlap=100`).

---

## 📄 License

MIT
```

