import itertools
N,K=map(int, input().split())
array=list(map(int, input().split()))
kitai=[]
for a in array:
    kitai.append((1+a)/2)
sums=list(itertools.accumulate(kitai))
ret=sums[K-1]
for i in range(K,N):
    ret=max(ret,sums[i]-sums[i-K])
print(ret)
