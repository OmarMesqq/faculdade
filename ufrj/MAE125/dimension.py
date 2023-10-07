import numpy as np

def span_dimension(vectors):
    # Convert the list of vectors to a numpy array
    vectors = np.array(vectors)
    
    # Find the rank of the matrix whose rows are the vectors
    rank = np.linalg.matrix_rank(vectors)
    
    # Return the rank as the dimension of the span
    return rank


v1 = [1, -2, -1, -1, 1, -2]
v2 = [-1, 3, 2, -1, 0, 1] 
v3 = [2, -3, -2, -5, 5, -7]
v4 = [-2, 6, 3, -5, 3, 2]
v5 = [-2, 3, -1, 0, 0, 1]
v6 = [2, -2, 1, -1, 2, -6] 

dim = span_dimension([v1, v2, v3, v4, v5, v6])

print("Dimension of span:", dim)
