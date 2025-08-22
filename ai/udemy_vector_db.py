import os
import chromadb
from dotenv import load_dotenv
from chromadb.utils import embedding_functions
# from langchain_community.embeddings import HuggingFaceEmbeddings

chromadb_client = chromadb.PersistentClient(path="./udemy_chroma_db")

embedding_model = embedding_functions.OllamaEmbeddingFunction()

collection_name = "document_qa_collection"
collection = chromadb_client.get_or_create_collection(name=collection_name, embedding_function=embedding_model)


def load_documents_from_directory(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                documents.append({"id": filename, "text": file.read})
    return documents

def split_text(text, chunk_size=1000, chunk_overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks

directory_path = "./new_articles"
documents = load_documents_from_directory(directory_path)

print(f"Loaded {len(documents)} documents from {directory_path}")