import chromadb


#client
client = chromadb.PersistentClient(path="Cdatabase")

collection = client.create_collection(name="books")


collection.add(
    documents=[
        "Dogs are loyal animals.",
        "Python is a programming language.",
        "Artificial Intelligence."
    ],
    ids=[
        "1",
        "2",
        "3"
    ]
)

results = collection.query(
    query_texts=["AI"],
    n_results=2
)


print(results)