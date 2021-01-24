from collections import defaultdict
import copy
W=int(input())
N,K=map(int, input().split())
dp=[[0]*(W+1) for i in range(K+1)]
for i in range(N):
    a,b=map(int, input().split())
    if a>W:
        continue
    for i in range(W-a+1)[::-1]:
        for j in range(K)[::-1]:
            dp[j+1][i+a]=max(dp[j+1][i+a],dp[j][i]+b)
print(dp[K][W])
