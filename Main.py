import SLsearch as SL
import Lsearch as L
import Bsort as B
import Qsort as Q

print('how many times?')
times = int(raw_input())

SL.SLsearch(times)

L.Lsearch(times)

a = B.bubblesort(times)
print a

a = Q.quicksort(times)
print a
