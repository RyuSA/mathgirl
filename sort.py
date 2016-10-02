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

def QUICK_SORT(A,L,R):
    if L < R:
        # if you wanna compare QUICK_SORT and RANDOMIZED_QUICK_SORT, you may use randint
        np.random.randint(L,R)
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

def RANDOMIZED_QUICK_SORT(A,L,R):
    if L < R:
        r = np.random.randint(L,R)
        A[L], A[r] = A[r], A[L]
        p = L
        k = L+1
        while k <= R:
            if A[k] < A[L]:
                A[p+1], A[k] = A[k], A[p+1]
                p += 1
            k += 1
        A[L], A[p] = A[p], A[L]
        A = RANDOMIZED_QUICK_SORT(A,L,p-1)
        A = RANDOMIZED_QUICK_SORT(A,p+1,R)
    return A
