import numpy as np
import time

start = time.time()

def BOGO_SORT(A):
    set_range = range(0,A.size -1)
    # if A is ssorted, ignore while
    while not isSorted(A,set_range):
        np.random.shuffle(A)

def isSorted(B,Range):
    for i in Range:
        # if there exist some illegal in the given array, return false
        if B[i] > B[i+1]:
            return False
    return True

# measure time from here
start = time.time()

# set the range for random
Min = 1
Max = 10
N = Max
# get a list consisted by N random integers in [min,max]
LIST = np.random.randint(Min,Max,N)

# sorting by bubble
BOGO_SORT(LIST)

print LIST
print str(time.time()-start) + 'sec'
