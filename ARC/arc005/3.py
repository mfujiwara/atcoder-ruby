import sys
H,W=map(int, input().split())
MAP=[input() for _ in range(H)]
targets=[]
costs=[]
for i in range(H):
    costs.append([])
    for j in range(W):
        if MAP[i][j]=="s":
            targets.append((i,j))
            costs[-1].append(0)
        else:
            costs[-1].append(-1)

next_targets=[]
while targets:
    h,w=targets.pop()
    if MAP[h][w]=="g":
        print("YES")
        sys.exit()
    if h>0 and costs[h-1][w]==-1:
        if MAP[h-1][w]=="#":
            next_targets.append((h-1,w))
            costs[h-1][w]=costs[h][w]+1
        else:
            targets.append((h-1,w))
            costs[h-1][w]=costs[h][w]
    if w>0 and costs[h][w-1]==-1:
        if MAP[h][w-1]=="#":
            next_targets.append((h,w-1))
            costs[h][w-1]=costs[h][w]+1
        else:
            targets.append((h,w-1))
            costs[h][w-1]=costs[h][w]
    if h<H-1 and costs[h+1][w]==-1:
        if MAP[h+1][w]=="#":
            next_targets.append((h+1,w))
            costs[h+1][w]=costs[h][w]+1
        else:
            targets.append((h+1,w))
            costs[h+1][w]=costs[h][w]
    if w<W-1 and costs[h][w+1]==-1:
        if MAP[h][w+1]=="#":
            next_targets.append((h,w+1))
            costs[h][w+1]=costs[h][w]+1
        else:
            targets.append((h,w+1))
            costs[h][w+1]=costs[h][w]
    if not targets and costs[h][w]!=2:
        targets=next_targets
        next_targets=[]
print("NO")
