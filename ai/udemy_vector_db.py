import os
import chromadb
from dotenv import load_dotenv
from chromadb.utils import embedding_functions

chromadb_client = chromadb.PersistentClient(path="./db/udemy_chroma_db")

embedding_model =  embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L6-v2")

collection_name = "document_qa_collection"
collection = chromadb_client.get_or_create_collection(name=collection_name, embedding_function=embedding_model)

def load_documents_from_directory(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                documents.append({"id": filename, "text": file.read()})
    return documents

def split_text(text, chunk_size=1000, chunk_overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks


# MAIN


directory_path = "./input-data/articles"
documents = load_documents_from_directory(directory_path)

# Split documents into chunks
chunked_documents = []
for doc in documents:
    chunks = split_text(doc["text"])
    print("========Splitting documents into chunks ========")
    for i, chunk in enumerate(chunks):
        chunked_documents.append({"id": f"{doc['id']}_chunk_{i+1}", "text": chunk})

# def generate_embeddings(text):
#     print("========Generating embeddings for chunks ========")
#     return embedding_model.embed_documents(text)

# for doc in chunked_documents:
#     print("Calling generate_embeddings function")
#     doc["embedding"] = generate_embeddings(doc["text"])

# Upsert directly (Chroma will call embedding_model internally)
for doc in chunked_documents: 
    print(f"Upserting document ID: {doc['id']}")
    collection.upsert(
        documents=[doc["text"]],
        ids=[doc["id"]]
        # embeddings=[doc["embedding"]]
    )

print("✅ Documents successfully upserted into ChromaDB!")
