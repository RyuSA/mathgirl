import numpy as np
import math
import random
import time

start = time.time()

def BINARY_SEARCH(A,n,v):
    a = 0
    b = n-1
    while  a <= b :
        k = int(math.floor((a+b)/2))
        if A[k] == v:
            return 'found'
        elif A[k] < v:
            a = k+1
        else:
            b = k-1
    return 'not found'

# Define the range
Min = 1
Max = 10000000

# Sub A, n, v
N = Max
LIST = np.random.randint(Min,Max,N)
# quick sort
# LIST = np.sort(LIST,kind='mergesort')
LIST = np.sort(LIST)
V = random.randint(Min,Max)
result = BINARY_SEARCH(LIST,N,V)
result_time = time.time()-start

print 'serch ' + str(V) + ' from ' + str(LIST)
print result
print str(result_time) + 'sec'
