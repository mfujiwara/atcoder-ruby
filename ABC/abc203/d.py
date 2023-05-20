N,K=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(N)]
left=-1
right=10**9
while True:
    if left+1==right:
        print(right)
        exit()
    mid=(left+right)//2
    dp=[[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            v=0
            if i>0:
                v+=dp[i-1][j]
            if j>0:
                v+=dp[i][j-1]
            if i>0 and j>0:
                v-=dp[i-1][j-1]
            if A[i][j]<=mid:
                v+=1
            dp[i][j]=v
    r=0
    for i in range(K-1,N):
        for j in range(K-1,N):
            v=dp[i][j]
            if i>K-1:
                v-=dp[i-K][j]
            if j>K-1:
                v-=dp[i][j-K]
            if i>K-1 and j>K-1:
                v+=dp[i-K][j-K]
            r=max(r,v)
    if r>=(K*K+1)//2:
        right=mid
    else:
        left=mid
