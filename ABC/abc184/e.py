from collections import defaultdict
import sys
H,W=map(int, input().split())
MAP=[input() for i in range(H)]
s=None
g=None
warps=defaultdict(list)
for i in range(H):
    for j in range(W):
        ch=MAP[i][j]
        if ch=="S":
            s=(i,j)
        elif ch=="G":
            g=(i,j)
        elif ch=="#" or ch==".":
            continue
        else:
            warps[ch].append((i,j))
r=0
starts=[s]
goals=[g]
REACHED=[ [0]*W for _ in range(H) ]
i,j=s
REACHED[i][j]=1
i,j=g
REACHED[i][j]=2
def get_nexts(i,j):
    nexts=[]
    if i>0 and MAP[i-1][j]!="#":
        nexts.append((i-1,j))
    if i<H-1 and MAP[i+1][j]!="#":
        nexts.append((i+1,j))
    if j>0 and MAP[i][j-1]!="#":
        nexts.append((i,j-1))
    if j<W-1 and MAP[i][j+1]!="#":
        nexts.append((i,j+1))
    for (k,l) in warps[MAP[i][j]]:
        if i!=k or j!=l: nexts.append((k,l))
    warps[MAP[i][j]]=[]
    return nexts
while len(starts)!=0 and len(goals)!=0:
    nexts_s=[]
    r+=1
    for (i,j) in starts:
        for (k,l) in get_nexts(i,j):
            if REACHED[k][l]==2:
                print(r)
                sys.exit()
            if REACHED[k][l]!=1:
                nexts_s.append((k,l))
                REACHED[k][l]=1
    starts=nexts_s
    nexts_g=[]
    r+=1
    for (i,j) in goals:
        for (k,l) in get_nexts(i,j):
            if REACHED[k][l]==1:
                print(r)
                sys.exit()
            if REACHED[k][l]!=2:
                nexts_g.append((k,l))
                REACHED[k][l]=2
    goals=nexts_g
print("-1")
