N,M=map(int, input().split())
A=[list(input()) for _ in range(2*N)]
ranks=[(0,i) for i in range(N*2)]
for j in range(M):
    nexts=[]
    for i in range(N):
        n1,i1=ranks[i*2]
        n2,i2=ranks[i*2+1]
        if A[i1][j]=="G" and A[i2][j]=="C" or A[i1][j]=="C" and A[i2][j]=="P" or A[i1][j]=="P" and A[i2][j]=="G":
            n1-=1
        elif A[i1][j]=="G" and A[i2][j]=="P" or A[i1][j]=="C" and A[i2][j]=="G" or A[i1][j]=="P" and A[i2][j]=="C":
            n2-=1
        nexts.append((n1,i1))
        nexts.append((n2,i2))
    nexts.sort()
    ranks=nexts
for _,i in ranks:
    print(i+1)
