import itertools
N=int(input())
array=list(map(int, input().split()))
sums=list(itertools.accumulate(array))+[0]
sums=sorted([s%360 for s in sums])
ret=0
for i in range(N+1):
    r=(sums[(i+1)%(N+1)]-sums[i]+360)%360
    ret=max(ret,r)
print(ret)
