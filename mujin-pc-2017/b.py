N=int(input())
A=[[0]*N for _ in range(N)]
some=False
all=True
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            A[i][j]=1
            some=True
        else:
            all=False
if not some:
    print(-1)
    exit()
if all:
    print(0)
    exit()
c=0
for j in range(N):
    for i in range(N):
        if A[i][j]==0:
            c+=1
            break
ret=c+N+1
for i in range(N):
    x=N-sum(A[i])+1
    for j in range(N):
        if A[j][i]==1:
            x-=1
            break
    ret=min(ret,x+c)
print(ret)
