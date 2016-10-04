import numpy as np
import random
import time
import search

def SLsearch(howmany):
    # Define the range
    Min = 1
    Max = 100000

    # Sub A, n, v
    f = open('SLsearch.txt','w')

    LIST = np.random.randint(Min,Max,Max)

    for i in xrange(howmany):
        start = time.time()
        V = random.randint(Min,Max)
        search.SENTINEL_LINER_SERCH(LIST,Max,V)
        result_time = str(time.time()-start)
        f.write(result_time)
        f.write('\n')

    print('Slinear search done')
    f.close()
