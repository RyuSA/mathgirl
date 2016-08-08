import time
import numpy as np

def QUICK_SORT(A,L,R):
    if L < R:
        p = L
        k = L+1
        while k <= R:
            if A[k] < A[L]:
                A[p+1], A[k] = A[k], A[p+1]
                p += 1
            k += 1
        A[L], A[p] = A[p], A[L]
        A = QUICK_SORT(A,L,p-1)
        A = QUICK_SORT(A,p+1,R)
    return A

# mesure time from here
start = time.time()

# set the range for random
Min = 1
Max = 1000
N = Max

# get a list consisted by N random integers in [min,max]
LIST = np.random.randint(Min,Max,N)
N -= 1

# sort by quick
LIST = QUICK_SORT(LIST,0,N)

print LIST
print str(time.time()-start) + 'sec'
