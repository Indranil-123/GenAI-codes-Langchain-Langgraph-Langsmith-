from sentence_transformers import SentenceTransformer
from conn import pc

INDEX_NAME = "ai-index"


index = pc.Index(INDEX_NAME)

model = SentenceTransformer("all-MiniLM-L6-V2")

documents = [
    "Artificial Intelligence is transforming healthcare.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Python is one of the best programming languages.",
    "Deep Learning uses neural networks.",
    "Pinecone is a cloud vector database."
]


vectors = []

for i, text in enumerate(documents):
    
    embedding = model.encode(text).tolist()
    
    vectors.append({
        "id": str(i),
        "values": embedding
    })
    

print(vectors)

index.upsert(vectors=vectors)

print("Successfully inserted vectors into Pincone")