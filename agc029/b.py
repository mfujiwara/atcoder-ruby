import bisect
from collections import defaultdict
N=int(input())
array=list(map(int, input().split()))
array=sorted(array)[::-1]
bekis=[2**(i+1) for i in range(30)]
hope_counts=defaultdict(int)
ret=0
for a in array:
    if hope_counts[a]>0:
        ret+=1
        hope_counts[a]-=1
    else:
        i=bisect.bisect_right(bekis,a)
        hope_counts[bekis[i]-a]+=1
print(ret)
