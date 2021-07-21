H,W,C=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H)]
ret=C*(H+W-2)+A[0][0]+A[-1][-1]
costs=[[0]*W for _ in range(H)] # 他の点からそこに到達するための最小コスト
for i in range(H):
    for j in range(W):
        if i==0 and j==0:
            costs[i][j]=A[i][j]
        elif i==0:
            costs[i][j]=costs[i][j-1]+C
            ret=min(ret,costs[i][j]+A[i][j])
            costs[i][j]=min(costs[i][j],A[i][j])
        elif j==0:
            costs[i][j]=costs[i-1][j]+C
            ret=min(ret,costs[i][j]+A[i][j])
            costs[i][j]=min(costs[i][j],A[i][j])
        else:
            costs[i][j]=min(costs[i-1][j],costs[i][j-1])+C
            ret=min(ret,costs[i][j]+A[i][j])
            costs[i][j]=min(costs[i][j],A[i][j])
for i in range(H-1,-1,-1):
    for j in range(W):
        if i==H-1 and j==0:
            costs[i][j]=A[i][j]
        elif i==H-1:
            costs[i][j]=costs[i][j-1]+C
            ret=min(ret,costs[i][j]+A[i][j])
            costs[i][j]=min(costs[i][j],A[i][j])
        elif j==0:
            costs[i][j]=costs[i+1][j]+C
            ret=min(ret,costs[i][j]+A[i][j])
            costs[i][j]=min(costs[i][j],A[i][j])
        else:
            costs[i][j]=min(costs[i+1][j],costs[i][j-1])+C
            ret=min(ret,costs[i][j]+A[i][j])
            costs[i][j]=min(costs[i][j],A[i][j])
print(ret)
