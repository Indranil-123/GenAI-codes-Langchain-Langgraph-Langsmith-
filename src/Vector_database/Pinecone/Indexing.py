import time 
from pinecone import ServerlessSpec
from conn import pc


INDEX_NAME ="ai-index"
DIMENSION = 384
METRIC = "cosine"


existing_indexes = [index.name for index in pc.list_indexes().indexes]


if INDEX_NAME in existing_indexes:
    print("index already exists. ")
else:
    try:
        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric=METRIC,
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
            
        )
        
        while not pc.describe_index(INDEX_NAME).status["ready"]:
            print("⏳ Waiting for index to become ready...")
            time.sleep(2)

        print(f"✅ Index '{INDEX_NAME}' created successfully!")
        
        index = pc.index(INDEX_NAME)
        
        stats = index.describe_index_stats()

        print("\n📊 Index Statistics")
        print("-" * 40)
        print(f"Dimension          : {stats['dimension']}")
        print(f"Total Vectors      : {stats['total_vector_count']}")
        print(f"Index Fullness     : {stats['index_fullness']}")
        print(f"Namespaces         : {stats['namespaces']}")
        
        
    except:
        print("there is a exception")
        
        
    