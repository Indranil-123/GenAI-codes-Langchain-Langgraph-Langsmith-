import chromadb

client = chromadb.PersistentClient(path="newdb")

collection = client.get_or_create_collection(
    name="books",
    metadata={
        "description": "A collection of books",
        "author": "John Doe"
    }
    
    )

collection.add(
    documents=[
        "The Great Gatsby",
        "To Kill a Mockingbird",
    ],
    metadata=[
        {"genre": "Fiction", "year": 1925},
        {"genre": "Fiction", "year": 1960}
    ],
    ids=[
        "1",
        "2"
    ]
)