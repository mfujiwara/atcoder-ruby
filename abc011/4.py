N,D=map(int, input().split())
X,Y=map(int, input().split())
x,r1=divmod(X,D)
y,r2=divmod(Y,D)
if r1!=0 or r2!=0 or x+y>N or (x+y)%2!=N%2:
    print(0)
    exit()
x=abs(x)
y=abs(y)
dp=[[0]*(N+1) for _ in range(N+1)]
dp[0][0]=1
for k in range(N):
    for i in range(N):
        dp[k+1][i]+=dp[k][i]
        dp[k+1][i+1]+=dp[k][i]
ret=0
for i in range(x,N-y+1,2):
    di=(i-x)//2
    j=N-i
    dj=(j-y)//2
    rx=dp[N][x+di]
    ri=dp[N-x-di][di]
    ry=dp[N-i][y+dj]
    ret+=rx*ri*ry
print(ret/pow(4,N))
