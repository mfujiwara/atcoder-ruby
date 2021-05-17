H,W=map(int, input().split())
A=[]
for _ in range(H):
    array=[]
    for c in list(input()):
        if c=="+":
            array.append(1)
        else:
            array.append(-1)
    A.append(array)
INF=10**10
dp=[[INF]*W for _ in range(H)]

def calc(i,j):
    if dp[i][j]!=INF:
        return dp[i][j]

    now_score= A[i][j] if (i+j)%2==1 else -A[i][j]
    if i==H-1 and j==W-1:
        dp[i][j]=now_score
        return dp[i][j]
    if i==H-1:
        dp[i][j]=now_score + dp[i][j+1]
        return dp[i][j]
    if j==W-1:
        dp[i][j]=now_score + dp[i+1][j]
        return dp[i][j]
    s1=dp[i+1][j]
    s2=dp[i][j+1]
    if (i+j)%2==0:
        if s1>s2:
            dp[i][j]=s1+now_score
            return dp[i][j]
        else:
            dp[i][j]=s2+now_score
            return dp[i][j]
    else:
        if s1>s2:
            dp[i][j]=s2+now_score
            return dp[i][j]
        else:
            dp[i][j]=s1+now_score
            return dp[i][j]
for i in range(H)[::-1]:
    for j in range(W)[::-1]:
        calc(i,j)
ret=dp[0][0]+A[0][0]
if ret>0:
    print("Takahashi")
elif ret<0:
    print("Aoki")
else:
    print("Draw")
