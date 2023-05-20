N,M,Q=map(int, input().split())
S=[list(map(int, list(input()))) for _ in range(N)]
a = [[0]*(M+1) for _ in range(N+1)]
b = [[0]*(M+1) for _ in range(N)]
c = [[0]*(M) for _ in range(N+1)] 
for i in range(N):
    for j in range(M):
        if S[i][j]==1:
            a[i+1][j+1] = 1
for i in range(N-1):
    for j in range(M):
        if S[i][j]==1 and S[i+1][j]==1:
            b[i+1][j+1] = 1
for i in range(N):
    for j in range(M-1):
        if S[i][j]==1 and S[i][j+1]==1:
            c[i+1][j+1] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        a[i][j] += a[i-1][j]
for i in range(1,N+1):
    for j in range(1,M+1):
        a[i][j] += a[i][j-1]
for i in range(1,N):
    for j in range(1,M+1):
        b[i][j] += b[i-1][j]
for i in range(1,N):
    for j in range(1,M+1):
        b[i][j] += b[i][j-1]
for i in range(1,N+1):
    for j in range(1,M):
        c[i][j] += c[i-1][j]
for i in range(1,N+1):
    for j in range(1,M):
        c[i][j] += c[i][j-1]
for _ in range(Q):
    x,y,z,w=map(int, input().split())
    A = a[z][w]-a[z][y-1]-a[x-1][w]+a[x-1][y-1]
    B = b[z-1][w]-b[z-1][y-1]-b[x-1][w]+b[x-1][y-1]
    C = c[z][w-1]-c[z][y-1]-c[x-1][w-1]+c[x-1][y-1]
    #print(A,B,C)
    print(A-B-C)
