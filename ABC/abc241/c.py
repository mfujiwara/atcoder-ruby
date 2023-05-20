N=int(input())
S=[[0]*N for _ in range(N)]
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            S[i][j]=1
for i in range(N):
    total=0
    for j in range(N):
        total+=S[i][j]
        if j>=6:
            total-=S[i][j-6]
        if total>=4:
            print("Yes")
            exit()
for j in range(N):
    total=0
    for i in range(N):
        total+=S[i][j]
        if i>=6:
            total-=S[i-6][j]
        if total>=4:
            print("Yes")
            exit()
for i in range(6-N,N-5):
    total=0
    for j in range(N):
        if i+j<0: continue
        if i+j>=N: break
        total+=S[i+j][j]
        if j>=6 and i+j-6>=0:
            total-=S[i+j-6][j-6]
        if total>=4:
            print("Yes")
            exit()
for i in range(5,2*N-6):
    total=0
    for j in range(N):
        if i-j>=N: continue
        if i-j<0: break
        total+=S[i-j][j]
        if j>=6 and i-j+6<N:
            total-=S[i-j+6][j-6]
        if total>=4:
            print("Yes")
            exit()
print("No")
