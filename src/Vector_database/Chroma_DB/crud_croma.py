import chromadb

client = chromadb.PersistentClient(path="newdbs")

#create a collection with metadata
collection = client.get_or_create_collection(
    name="movies",
    metadata={
        "description": "A collection of movies",
        "curator": "Jane Smith"
    }
)

#create read Update Delete (CRUD) operations for the collection
def add_movie(document, metadata, id):
    collection.add(
        documents=[document],
        metadata=[metadata],
        ids=[id]
    )
    return f"Movie '{document}' added successfully."

def get_movie(id):
    result = collection.get(ids=[id])
    return result

def update_movie(id, new_document=None, new_metadata=None):
    if new_document:
        collection.update(
            ids=[id],
            documents=[new_document]
        )
    if new_metadata:
        collection.update(
            ids=[id],
            metadata=[new_metadata]
        )
        
    else:
        return "No updates provided."
    return f"Movie with ID '{id}' updated successfully."