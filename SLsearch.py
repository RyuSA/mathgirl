import numpy as np
import time

start = time.time()

def SENTINEL_LINER_SERCH(A,n,v):
    np.append(A,v)
    k = 1
    while  A[k] != v:
        k += 1
    if k <= n:
        return 'found'
    return '404'

# Define the range
Min = 1
Max = 10000000

# Sub A, n, v
N = Max
LIST = np.random.randint(Min,Max,N)
V = np.random.randint(Min,Max,1)
result = SENTINEL_LINER_SERCH(LIST,N,V)
result_time = time.time()-start

print result
print str(result_time) + 'sec'
