INF=pow(10,18)
H,W,K=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H)]
# 全要素に順番をつける
array=[]
for i in range(H):
    for j in range(W):
        array.append((A[i][j],i,j))
array.sort()
rank=[[0]*W for i in range(H)]
for r in range(H*W):
    _, i, j = array[r]
    rank[i][j]=r
ret=INF
for low in range(H*W):
    # rankがlowのものがK番目になるような経路を考える
    X=array[low][0]
    B=[[max(0,A[i][j]-X) for j in range(W)] for i in range(H)]
    dp=[[INF]*W for _ in range(H)]
    dp[0][0]=B[0][0]
    for i in range(H):
        for j in range(W):
            if i==0 and j==0: continue
            if i>0:
                dp[i][j]=min(dp[i][j],dp[i-1][j]+B[i][j])
            if j>0:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+B[i][j])
    ret=min(ret,dp[-1][-1]+X*K)
print(ret)
