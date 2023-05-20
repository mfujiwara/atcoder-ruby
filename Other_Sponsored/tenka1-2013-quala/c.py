M,N=map(int, input().split())
if M>N:
    M,N=N,M
if M>20:
    M=20+M%4
if N>20:
    N=20+N%4
matrix=[[0]*(N+3) for _ in range(M+3)]
targets=[(0,0,1),(0,0,2),(0,0,3)]
ret=0
while targets:
    x,y,v=targets.pop()
    matrix[x+3][y+3]=v
    if x==M-1 and y==N-1:
        ret+=1
        continue
    ux = x if y<N-1 else x+1
    uy = y+1 if y<N-1 else 0
    if matrix[ux+2][uy+3]!=1 and matrix[ux+3][uy+2]!=1:
        targets.append((ux,uy,1))
    if matrix[ux+2][uy+3]!=2 and matrix[ux+3][uy+2]!=2 and matrix[ux+1][uy+3]!=2 and matrix[ux+3][uy+1]!=2:
        targets.append((ux,uy,2))
    if matrix[ux+2][uy+3]!=3 and matrix[ux+3][uy+2]!=3 and matrix[ux+1][uy+3]!=3 and matrix[ux+3][uy+1]!=3 and matrix[ux][uy+3]!=3 and matrix[ux+3][uy]!=3:
        targets.append((ux,uy,3))
print(ret)
