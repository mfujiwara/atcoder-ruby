H,W=map(int, input().split())
B=[[0]*H for _ in range(W)]
for i in range(H):
    for j,a in enumerate(list(map(int, input().split()))):
        B[j][i]=a
for i in range(W):
    print(*B[i])
