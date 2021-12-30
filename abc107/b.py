H,W=map(int, input().split())
rows=set()
cols=set()
A=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="#":
            A[i][j]=1
            rows.add(i)
            cols.add(j)
rows=sorted(list(rows))
cols=sorted(list(cols))
for i in rows:
    for j in cols:
        if A[i][j]==0:
            print(".",end="")
        else:
            print("#",end="")
    print()
