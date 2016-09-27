import numpy as np
import math

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

def BINARY_SEARCH(A,n,v):
    a = 0
    b = n-1
    while  a <= b :
        k = int(math.floor(b + (a-b)/2))
        if A[k] == v:
            return True
        elif A[k] < v:
            a = k+1
        else:
            b = k-1
    return False
