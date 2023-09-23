import itertools
import bisect
N,M,P=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_array.sort()
b_array.sort()
a_sums=list(itertools.accumulate(a_array))
b_sums=list(itertools.accumulate(b_array))
ret=0
for a in a_array:
    i=bisect.bisect(b_array,P-a)
    if i>0:
        ret+=b_sums[i-1]+a*i
    ret+=P*(M-i)
print(ret)
