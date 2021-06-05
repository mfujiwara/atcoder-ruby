MOD=10**9+7
N,K=map(int, input().split())
all_counts=[0]*(K+1)
for i in range(1,K+1):
    all_counts[i]=pow(K//i,N,MOD)
counts=[0]*(K+1)
for i in range(K,0,-1):
    counts[i]=all_counts[i]
    k=i*2
    while k<=K:
        counts[i]-=counts[k]
        counts[i]%=MOD
        k+=i
ret=0
for i in range(1,K+1):
    ret+=i*counts[i]
    ret%=MOD
ret=(ret+MOD)%MOD
print(ret)
