import time
import numpy as np

start = time.time()

# def EXCHANGE(a,b):
#     temp = a
#     a = b
#     b = temp

def BUBBLE_SORT(A,n):
    m = n-1
    while  m > 1:
        k = 0
        while k < m :
            if A[k] > A[k+1]:
                temp = A[k]
                A[k] = A[k+1]
                A[k+1] = temp
            k += 1
        m -= 1
    return A

Min = 1
Max = 1000

N = Max
LIST = np.random.randint(Min,Max,N)

BUBBLE_SORT(LIST,N)


print LIST
print str(time.time()-start) + 'sec'
