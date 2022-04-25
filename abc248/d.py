import bisect
import collections
N=int(input())
array=list(map(int, input().split()))
indexes=collections.defaultdict(list)
for i,a in enumerate(array):
    indexes[a].append(i)
Q=int(input())
for _ in range(Q):
    l,r,x=map(int, input().split())
    l-=1
    r-=1
    ll=bisect.bisect_left(indexes[x],l)
    rr=bisect.bisect_right(indexes[x],r)
    print(rr-ll)
