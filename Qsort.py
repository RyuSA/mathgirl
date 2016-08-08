import time
import numpy as np

start = time.time()
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

Min = 1
Max = 1000

N = Max
LIST = np.random.randint(Min,Max,N)
N -= 1


LIST = QUICK_SORT(LIST,0,N)

print LIST
print str(time.time()-start) + 'sec'
