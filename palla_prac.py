import time
# import multiprocessing as mp
from multiprocessing import Pool
from multiprocessing import Process

start = time.time()

def function(N):
    return N

def multi(n):
    p = Pool(2)
    result = p.map(function, range(n))
    return result

def main():
    data = multi(5)
    for i in data:
        print i

main()

print time.time()-start
