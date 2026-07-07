import numpy as np



A = np.array([2,3])
B = np.array([5,7])


#euclidean distance hardcoded
def euclidean_hard_coded(a,b):
    distance = np.sqrt(np.sum((a-b)**2))
    return distance


#euclidean distance automated form
def euclidean_automated(a,b):
    distance = np.linalg.norm(a-b)
    return distance

def manhattan_distance(a,b):
    #formula |x2-x1| + |y2-y1|
    distance = np.sum(np.abs(a-b))
    return distance


def dot_product(a,b):
    #formula |x2*x1| + |y2*y1|
    dist1 = np.dot(a,b)
    dist2 = a @ b
    return dist1, dist2

def cosine_similar(a,b):
    dot = np.dot(a,b)
    norm1 = np.linalg.norm(a)
    norm2 = np.linalg.norm(b)
    
    dist = dot / (norm1 * norm2)
    return dist  