# Write a function that normalize a 2D matrix (zero mean and unit variant) column-wise
# Formula: f(X) = X-mean(X) / sigma(X) where X is a column
# sigma: standard deviation = sqrt(variance)
# variance: mean( ( X-mean(X) )*( X-mean(X) ) )

import numpy as np


# Using indexing and broadcasting 
def normalize1(arr: np.ndarray):
    meanCols = (np.sum(arr, 0)/ arr.shape[0]).reshape(1, arr.shape[1])
    sigmaCols = ( np.sqrt( np.sum( ( arr - meanCols)**2, 0 )  /  arr.shape[0] ) ).reshape(1, arr.shape[1])
    return (arr - meanCols)/sigmaCols


# Using loop and some indexing
def normalize2(arr:np.ndarray):

    for i in range(arr.shape[1]):
        meanCol = np.sum(arr[: , i])/arr.shape[0]
        sigmaCol = np.sqrt( np.mean( (arr[:, i] - meanCol)**2) )
        arr[: , i] = ( arr[: , i] - meanCol) / sigmaCol 
    return arr



A = np.random.randint(-5, 5, (4, 5)).astype(np.float32)
print(A)
print(normalize1(A))
print(normalize2(A))
