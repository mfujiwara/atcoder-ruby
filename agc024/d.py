N=int(input())
M=2*N-1
edges=[[] for _ in range(M)]
for i in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    c=N+i
    # 中間点をおいて構成
    edges[a].append(c)
    edges[c].append(a)
    edges[b].append(c)
    edges[c].append(b)
ret=[M,1<<64]
for i in range(M):
    # 各点を中心にした時に対称になるような木を考える
    targets=[i]
    depth=[-1]*M
    depth[i]=0
    depth_count=[0]*M
    while targets:
        t=targets.pop()
        c=0
        for u in edges[t]:
            if depth[u]!=-1: continue
            c+=1
            depth[u]=depth[t]+1
            targets.append(u)
        depth_count[depth[t]]=max(depth_count[depth[t]],c)
    # 葉の数を計算
    l=1
    for c in depth_count:
        if c==0:
            break
        l*=c
    # 同じ深さの点は同型なので
    ret=min(ret,[max(depth)//2+1,l])
print(*ret)
