import time

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

LIST = [3,4,6,2,5,0,82,1]
N = len(LIST)

BUBBLE_SORT(LIST,N)

print LIST
