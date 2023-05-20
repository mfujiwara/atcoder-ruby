H,W=map(int, input().split())
C=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="#":
            C[i][j]=1
def calc(start):
    ret=-1
    targets=[[start]]
    while targets:
        nexts=[]
        for t in targets:
            r,c=t[-1]
            if r>0 and (r-1,c) not in t and C[r-1][c]==0:
                u=t[:]
                u.append((r-1,c))
                nexts.append(u)
            if r<H-1 and (r+1,c) not in t and C[r+1][c]==0:
                u=t[:]
                u.append((r+1,c))
                nexts.append(u)
            if c>0 and (r,c-1) not in t and C[r][c-1]==0:
                u=t[:]
                u.append((r,c-1))
                nexts.append(u)
            if c<W-1 and (r,c+1) not in t and C[r][c+1]==0:
                u=t[:]
                u.append((r,c+1))
                nexts.append(u)
            if len(t)>=3 and abs(start[0]-t[-1][0])+abs(start[1]-t[-1][1])==1:
                #print(t)
                ret=max(ret,len(t))
        targets=nexts
    return ret
rrr=-1
for i in range(H):
    for j in range(W):
        if C[i][j]==0:
            r=calc((i,j))
            rrr=max(rrr,r)
print(rrr)
