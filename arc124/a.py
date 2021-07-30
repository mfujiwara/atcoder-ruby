MOD=998244353
N,K=map(int, input().split())
count=[[1]*K for _ in range(N)]
for i in range(K):
    c,k=input().split()
    k=int(k)-1
    count[k]=[0]*K
    count[k][i]=1
    if c=="L":
        for j in range(k-1,-1,-1):
            count[j][i]=0
    else:
        for j in range(k+1,N):
            count[j][i]=0
ret=1
for c in count:
    ret*=sum(c)
    ret%=MOD
print(ret)
