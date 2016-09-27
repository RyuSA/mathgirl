import time
import numpy as np
import sort

def rquicksort(howmany):
    # set the range for random
    Min = 1
    Max = 1000

    f = open('RQuicksort.txt','w')
    for i in xrange(howmany):
        # get a list consisted by N random integers in [min,max]
        LIST = np.random.randint(Min,Max,Max)
        start = time.time()
        # sort by quick
        LIST = sort.RANDOMIZED_QUICK_SORT(LIST,0,Max-1)
        result_time = str(time.time()-start)
        f.write(result_time)
        f.write('\n')
    print('quicksort done')
    f.close()
    return LIST
