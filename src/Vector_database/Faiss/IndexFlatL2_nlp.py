import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Dogs are loyal animals",

    "Python is a programming language",

    "Machine Learning is amazing",

    "Artificial Intelligence"
]


#generate emddings
embeddings = embedding_model.encode(documents)

#convert to float32 
embeddings = np.array(embeddings).astype('float32')

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

query = "Tell me about AI"

query_embedding = embedding_model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

distances, indices = index.search(query_embedding, k=2)

print("Distances:", distances)
print("Indices:", indices)

for rank, idx in enumerate(indices[0]):
    print(f"Rank {rank+1}")
    print("Document:", documents[idx])
    print("Distance:", distances[0][rank])
    print("-" * 50)