from numpy.random import np

# Define the range
Min = 1
Max = 100000

def LINER_SERCH(A,n,v):
    k = 1
    while  k < n:
        if A[k] == v:
            return True
        k += 1
    return False

def SENTINEL_LINER_SERCH(A,n,v):
    A = np.append(A,v)
    k = 0
    while  A[k] != v:
        k += 1
    if k < n:
        return True
    return False
