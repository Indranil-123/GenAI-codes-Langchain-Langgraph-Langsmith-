import os
from dotenv import load_dotenv
from pinecone import Pinecone


load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("PINECONE_API_KEY environment variable is not set.")

try:
    pc = Pinecone(api_key=api_key)
    
    indexes = pc.list_indexes()
    
    print("Pinecone client initialized successfully.")
    
    if len(indexes) == 0:
        print("No indexes found in Pinecone.")
    else:
        print(f"Found {len(indexes)} index(es) in Pinecone: {indexes}")
except Exception as e:
    raise ValueError(f"Failed to initialize Pinecone client: {e}")
