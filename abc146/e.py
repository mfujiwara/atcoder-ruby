import collections
N,K=map(int, input().split())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
counts[0]+=1
total=0
i2c={}
i2c[-1]=0
ret=0
for i,a in enumerate(array):
    if i>=K-1:
        c=i2c.pop(i-K)
        counts[c]-=1
        if counts[c]==0:
            counts.pop(c)
    total+=a-1
    total%=K
    ret+=counts[total]
    counts[total]+=1
    i2c[i]=total
print(ret)
