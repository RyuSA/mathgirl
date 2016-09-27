import SLsearch as SL
import Lsearch as L
import Bsearch
import Bsort
import Qsort as Q
import RQsort as RQ

print('how many times?')
times = int(raw_input())
#
# SL.SLsearch(times)
#
# L.Lsearch(times)
#
# Bsearch.Bsearch(times)
#
# a = Bsort.bubblesort(times)
# print a
#
a = Q.quicksort(times)
print a

a = RQ.rquicksort(times)
print a
