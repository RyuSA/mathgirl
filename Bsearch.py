import numpy as np
import random
import time
import search

def Bsearch(howmany):
    # Define the range
    Min = 1
    Max = 100000

    # Sub A, n, v
    f = open('Bsearch.txt','w')

    for i in xrange(howmany):
        V = random.randint(Min,Max)
        LIST = np.random.randint(Min,Max,Max)
        LIST = np.sort(LIST)
        start = time.time()
        search.BINARY_SEARCH(LIST,Max,V)
        result_time = str(time.time()-start)
        f.write(result_time)
        f.write('\n')

    print('done')
    f.close()
