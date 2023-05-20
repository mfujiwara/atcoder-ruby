INF=pow(10,20)
N=int(input())
txa=[[0]*5 for _ in range(pow(10,5)+1)]
for _ in range(N):
    t,x,a=map(int, input().split())
    txa[t][x]=a
dp=[-INF]*5
dp[0]=0
for i in range(1,pow(10,5)+1):
    nexts=[-INF]*5
    for j in range(5):
        if j==0:
            nexts[j]=max(dp[0:j+2])+txa[i][j]
        elif j==4:
            nexts[j]=max(dp[j-1:j+1])+txa[i][j]
        else:
            nexts[j]=max(dp[j-1:j+2])+txa[i][j]
    dp=nexts
    #print(dp)
print(max(dp))
