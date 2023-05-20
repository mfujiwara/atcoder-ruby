import itertools
MOD=998244353
N,D=map(int, input().split())
counts=[0,1]
for i in range(1,N):
    counts.append(counts[-1]*2%MOD)
sums=list(itertools.accumulate(counts))
ret=0
for i in range(D+1):
    j=D-i
    if i>=N or j>=N: continue
    # i上がってj下がる
    start=i
    if i<=j:
        end=N-1+i-j
    else:
        end=N-1
    c=(sums[end+1]-sums[start]+MOD)%MOD
    if i==0 or j==0:
        ret+=c*counts[j+1]%MOD
    else:
        ret+=c*counts[j]%MOD
    ret%=MOD
print(ret)
