H,W=map(int, input().split())
S=[[0]*W for _ in range(H)]
for i in range(H):
    s=input()
    for j,ch in enumerate(s):
        if ch=="#":
            S[i][j]=1
ranks=[[-1]*W for _ in range(H)]
ranks[0][0]=0
edges=[(0,0)]
def expand(edges, rank):
    rets=[]
    while edges:
        i,j=edges.pop()
        rets.append((i,j))
        for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=ni<H and 0<=nj<W and ranks[ni][nj]==-1 and S[ni][nj]==0:
                ranks[ni][nj]=rank
                edges.append((ni,nj))
    return rets
edges=expand(edges,0)
rank=1
while ranks[-1][-1]==-1:
    broken=[]
    for i,j in edges:
        for id in range(-2,3):
            ni=i+id
            for jd in range(-2,3):
                if abs(id)==2 and abs(jd)==2: continue
                nj=j+jd
                if 0<=ni<H and 0<=nj<W and ranks[ni][nj]==-1:
                    ranks[ni][nj]=rank
                    broken.append((ni,nj))
    edges=expand(broken,rank)
    rank+=1
print(ranks[-1][-1])
