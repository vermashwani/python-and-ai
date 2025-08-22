from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

# -----------------------------
# 1. Load your documents
# -----------------------------
def load_documents(file_path="policies.txt"):
    loader = TextLoader(file_path)
    return loader.load()

# -----------------------------
# 2. Split into chunks
# -----------------------------
def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

# -----------------------------
# 3. Build vector store
# -----------------------------
def build_vectorstore(docs):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )
    return vectorstore

# -----------------------------
# 4. Build RAG chain
# -----------------------------
def build_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = OllamaLLM(model="mistral")  # or "llama2"
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"   # simplest mode
    )
    return qa_chain

# -----------------------------
# 5. Run Queries
# -----------------------------
def main():
    docs = load_documents("policies.txt")
    chunks = split_documents(docs)
    vs = build_vectorstore(chunks)
    qa_chain = build_chain(vs)

    # Example queries
    queries = [
        # "How many casual leave days are allowed?",
        # "What is the dress code?",
        "How is remote work handled?"
    ]

    for q in queries:
        print(f"\nQ: {q}")
        answer = qa_chain.run(q)
        print(f"A: {answer}")

if __name__ == "__main__":
    main()
