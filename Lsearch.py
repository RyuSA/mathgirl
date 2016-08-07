from numpy.random import *
import time

start = time.time()

def LINER_SERCH(A,n,v):
    k = 1
    while  k < n:
        if A[k] == v:
            return 'found'
        k += 1
    return '404'

# Define the range
Min = 1
Max = 10000000

# Sub A, n, v
N = Max
LIST = randint(Min,Max,N)
V = randint(Min,Max,1)
result = LINER_SERCH(LIST,N,V)
result_time = time.time()-start

print result
print str(result_time) + 'sec'
