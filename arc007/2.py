N,M=map(int, input().split())
memo={}
for i in range(N+1):
    memo[i]=i
now=0
for _ in range(M):
    d=int(input())
    memo[now],memo[d]=memo[d],memo[now]
    now=d
rets=[0]*(N+1)
for i in range(0,N+1):
    rets[memo[i]]=i
for i in range(1,N+1):
    print(rets[i])
