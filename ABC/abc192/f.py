N,X=map(int, input().split())
array=list(map(int, input().split()))
ret=X-max(array)
for mod in range(2,N+1):
    dp=[[-1]*(N+1) for _ in range(mod)] # dp[i][j]:= j個選んで合計がi%modになる時の最大周数
    dp[0][0]=0
    for i,a in enumerate(array):
        updates=[]
        for j in range(mod):
            for k in range(N+1):
                if dp[j][k]==-1: continue
                val=dp[j][k]
                q,r=divmod(j+a,mod)
                updates.append((r,k+1,val+q))
        for r,k,v in updates:
            dp[r][k]=max(dp[r][k],v)
    q,r=divmod(X,mod)
    if dp[r][mod]!=-1:
        v=q-dp[r][mod]
        ret=min(ret,v)
print(ret)
