A,B=map(int, input().split())
def calc(c):
    if c==0: return 0
    C=list(map(int,list(str(c))))
    dp1=[0]*len(C)
    if C[0]!=4 and C[0]!=9:
        dp1[0]=1
    for i in range(1,len(C)):
        if C[i]!=4 and C[i]!=9:
            dp1[i]=dp1[i-1]*1
        else:
            dp1[i]=0
    dp=[[0]*10 for _ in range(len(C))]
    for i in range(1,C[0]):
        if i==4 or i==9: continue
        dp[0][i]+=1
    for i in range(1,len(C)):
        for j in range(10):
            if j==4 or j==9: continue
            dp[i][j]=sum(dp[i-1])
        if dp1[i-1]==1:
            for j in range(C[i]):
                if j==4 or j==9: continue
                dp[i][j]+=1
        for j in range(1,10):
            if j==4 or j==9: continue
            dp[i][j]+=1
    return sum(dp[-1])+dp1[-1]
a=calc(A-1)
b=calc(B)
print(B-A+1-(b-a))
