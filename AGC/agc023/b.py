N=int(input())
matrix=[input() for i in range(N)]
ret=0
for k in range(N):
    r=True
    for i in range(N-1):
        for j in range(N):
            x=(i+k)%N
            y=(j-k+N)%N
            if x==y+k: continue
            if matrix[i][j]!= matrix[y][x]:
                r=False
                break
    if r:
        ret+=1
print(ret*N)
