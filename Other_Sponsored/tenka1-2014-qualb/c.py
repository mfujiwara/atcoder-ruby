import enum


N=int(input())
C=[[0]*N for _ in range(N)]
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            C[i][j]=1
rets=[]
rets.append([0]*N)
for i in range(1,N):
    array=[]
    for j in range(N):
        v=0
        if i>1:
            v+=rets[i-2][j]
        if j>0:
            v+=rets[i-1][j-1]
        if j<N-1:
            v+=rets[i-1][j+1]
        if v%2==C[i-1][j]:
            array.append(0)
        else:
            array.append(1)
    rets.append(array)
for i in range(N):
    for j in range(N):
        if rets[i][j]==0:
            print(".",end="")
        else:
            print("#",end="")
    print("")
