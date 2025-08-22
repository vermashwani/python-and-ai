import chromadb
from sentence_transformers import SentenceTransformer

# chroma = chromadb.Client()
chroma = chromadb.PersistentClient(path="./db/chroma_db")
collection = chroma.get_or_create_collection("policies")

model = SentenceTransformer('all-MiniLM-L6-v2')

# Add docs
# collection.add(
#     documents=["Employees are entitled to 15 days casual leave", "Hello world"],
#     ids=["leave_1", "leave_2"],
#     embeddings=[model.encode("Employees are entitled to 15 days casual leave"), model.encode("Hello world")],
# )

# Query
q = "hello casual leave"
results = collection.query(
    query_embeddings=[model.encode(q)],
    n_results=3
)
print(results)
