import time
import numpy as np
import sort

def quicksort(howmany):
    # set the range for random
    Min = 1
    Max = 1000
    N = Max

    f = open('Quicksort.txt','w')
    for i in xrange(howmany):
        # get a list consisted by N random integers in [min,max]
        LIST = np.random.randint(Min,Max,N)
        N -= 1
        start = time.time()
        # sort by quick
        LIST = sort.QUICK_SORT(LIST,0,N)
        result_time = str(time.time()-start)
        f.write(result_time)
        f.write('\n')
    print('quicksort done')
    f.close()
    return LIST
