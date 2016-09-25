import time
import numpy as np
import sort

def bubblesort(howmany):
    # set the range for random
    Min = 1
    Max = 1000

    f = open('Bubblesort.txt','w')
    for i in xrange(howmany):
        # get a list consisted by N random integers in [min,max]
        LIST = np.random.randint(Min,Max,Max)
        start = time.time()
        # sort by bubble
        LIST = sort.BUBBLE_SORT(LIST)
        result_time = str(time.time()-start)
        f.write(result_time)
        f.write('\n')
    print('bubblesort done')
    f.close()
    return LIST
