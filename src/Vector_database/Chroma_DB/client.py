import chromadb


def create_chroma_client():
    """
    Create a Chroma client instance.

    Returns:
        chromadb.Client: An instance of the Chroma client.
    """
    return chromadb.Client()

def create_chroma_persistent_client(persist_directory):
    """
    Create a Chroma client instance with persistence.

    Args:
        persist_directory (str): The directory where the Chroma database will be persisted.

    Returns:
        chromadb.Client: An instance of the Chroma client with persistence.
    """
    return chromadb.Client(persist_directory=persist_directory)