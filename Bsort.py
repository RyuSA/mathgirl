import time
import numpy as np

def BUBBLE_SORT(A):
    n = np.size(A)
    m = n-1
    while  m > 1:
        k = 0
        while k < m :
            if A[k] > A[k+1]:
                A[k],A[k+1] = A[k+1],A[k]
            k += 1
        m -= 1
    return A

# mesure time from here
start = time.time()

# set the range for random
Min = 1
Max = 1000
N = Max
# get a list consisted by N random integers in [min,max]
LIST = np.random.randint(Min,Max,N)

# sorting by bubble
BUBBLE_SORT(LIST)

print LIST
print str(time.time()-start) + 'sec'
