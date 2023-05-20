N,M=map(int, input().split())
rets=[-1]*N
for _ in range(M):
    s,c=map(int, input().split())
    if N>1 and s==1 and c==0:
        print(-1)
        exit()
    if rets[s-1]==-1 or rets[s-1]==c:
        rets[s-1]=c
    else:
        print(-1)
        exit()
ret=0
for i in range(N):
    if N>1 and i==0:
        v=max(rets[i],1)
    else:
        v=max(rets[i],0)
    ret*=10
    ret+=v
print(ret)
