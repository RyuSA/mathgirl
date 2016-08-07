import random
import numpy as np
import time

start = time.time()

def SENTINEL_LINER_SERCH(A,n,v):
    print A
    A = np.append(A,v)
    print A
    k = 0
    while  A[k] != v:
        k += 1
    if k < n:
        return 'found'
    return '404'

# Define the range
Min = 1
Max = 10

# Sub A, n, v
N = Max
LIST = np.random.randint(Min,Max,N)
V = random.randint(Min,Max)
result = SENTINEL_LINER_SERCH(LIST,N,V)
result_time = time.time()-start

print result
print str(result_time) + 'sec'
