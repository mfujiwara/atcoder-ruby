S=[]
s=set()
for i in range(9):
    for j,ch in enumerate(input()):
        if ch=="#":
            S.append((i,j))
            s.add((i,j))
n=len(S)
ret=0
for i in range(n-1):
    for j in range(i+1,n):
        ax,ay=S[i]
        bx,by=S[j]
        diffx=bx-ax
        diffy=by-ay
        cx,cy=bx-diffy,by+diffx
        dx,dy=ax-diffy,ay+diffx
        if (cx,cy) in s and (dx,dy) in s:
            ret+=1
print(ret//2)
