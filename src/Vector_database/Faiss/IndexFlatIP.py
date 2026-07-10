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



#generate embeddings
embeddings = embedding_model.encode(documents)


#transform it into the float value
embeddings = np.array(embeddings).astype('float32')

faiss.normalize_L2(embeddings)


#find the dimention
dimension = embeddings.shape[1]

#create the index
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)


#our query
query = "Tell me about AI"

#encode
query_embedding = embedding_model.encode([query])

query_embedding = np.array(query_embedding).astype('float32')

#search
distance, indices = index.search(query_embedding,2)