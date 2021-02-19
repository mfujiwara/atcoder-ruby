N=int(input())
D=[list(map(int, input().split())) for _ in range(N)]
Q=int(input())
D_SUM=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        D_SUM[i][j]=D[i][j]
        if i>0: D_SUM[i][j]+=D_SUM[i-1][j]
        if j>0: D_SUM[i][j]+=D_SUM[i][j-1]
        if i>0 and j>0: D_SUM[i][j]-=D_SUM[i-1][j-1]
max_scores=[0]*(N**2+1)
for i1 in range(N):
    for j1 in range(N):
        for i2 in range(i1,N):
            for j2 in range(j1,N):
                score=D_SUM[i2][j2]
                if i1>0: score-=D_SUM[i1-1][j2]
                if j1>0: score-=D_SUM[i2][j1-1]
                if i1>0 and j1>0: score+=D_SUM[i1-1][j1-1]
                area=(i2-i1+1)*(j2-j1+1)
                max_scores[area]=max(max_scores[area], score)
for i in range(N**2):
    max_scores[i+1]=max(max_scores[i],max_scores[i+1])
for i in range(Q):
    p=int(input())
    print(max_scores[p])
