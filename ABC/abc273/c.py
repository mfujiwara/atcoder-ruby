import bisect
N=int(input())
array=list(map(int, input().split()))
sss=sorted(set(array))
l=len(sss)
rets=[0]*N
for a in array:
    i=bisect.bisect_right(sss, a)
    rets[l-i]+=1
for r in rets:
    print(r)
