import bisect
N=int(input())
array=[]
for _ in range(N):
    array.append(int(input()))
array=sorted(array)
indexes=[-1]*N
for i in range(N):
    indexes[i]=bisect.bisect_right(array,array[i]//2)
sums=[i for i in range(N+1)]
counts=[sums[indexes[i]] for i in range(N)]
tmp=[0]
for i in range(N):
    tmp.append(tmp[-1]+counts[i])
    sums=tmp
counts=[sums[indexes[i]] for i in range(N)]
tmp=[0]
for i in range(N):
    tmp.append(tmp[-1]+counts[i])
    sums=tmp
counts=[sums[indexes[i]] for i in range(N)]
print(sum(counts)%(10**9+7))
