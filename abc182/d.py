import itertools
N=int(input())
array=list(map(int, input().split()))
array=list(itertools.accumulate(array))
maxis=[array[0]]
for i in range(1,N):
    maxis.append(max(maxis[-1],array[i]))
array=list(itertools.accumulate(array))
ret=max(0,maxis[0])
for i in range(1,N):
    v=array[i-1]+maxis[i]
    ret=max(ret,v)
print(ret)
