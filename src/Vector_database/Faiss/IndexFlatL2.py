import faiss
import numpy as np

#embdeddings
embeddings = np.array([[1.0,2.0],
    [2.0,3.0],
    [4.0,5.0],
    [10.0,12.0]], dtype='float32')


print("Embeddings:")
print(embeddings)

#first task is to calculate the dimension
dimension = embeddings.shape[1]
print("Dimension:", dimension)


#create the index
index = faiss.IndexFlatL2(dimension)

#add the embeddings to the index
index.add(embeddings)

print(index.ntotal, "embeddings added to the index")


#searching
query = np.array([[2,2]], dtype='float32')


#search the index for the nearest neighbors
distances, indices = index.search(query, k=2)

print("Distances:")
print(distances)
print("Indices:")
print(indices)