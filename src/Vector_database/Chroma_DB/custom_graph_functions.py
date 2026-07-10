import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.utils import embedding_functions


client = chromadb.PersistentClient(path="newdb")

#embeddging functions
embedding_function = (
    embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

collection = client.create_collection(
    name="my_collection",
    embedding_function=embedding_function
)

collection.add(
    documents=[
        "This is the first document.",
        "This is the second document.",
        "This is the third document."
    ],
    
    ids=[
        "1",
        "2",
        "3"
    ]
)

results = collection.query(
    query_texts=[
        "Tell me about AI"
    ],
    n_results=2
    
)

print(results["documents"])