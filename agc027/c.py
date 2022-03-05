import collections
N,M=map(int, input().split())
s=[0 if ch=="A" else 1 for ch in list(input())]
edges=collections.defaultdict(set)
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].add(b)
    edges[b].add(a)
targets=set()
done=set()
for i in range(N):
    ss=set()
    for j in edges[i]:
        ss.add(s[j])
    if len(ss)!=2:
        done.add(i)
        for j in edges[i]:
            if i==j: continue
            edges[j].remove(i)
            targets.add(j)
        edges[i].clear()
while targets:
    t=targets.pop()
    ss=set()
    for u in edges[t]:
        ss.add(s[u])
    if len(ss)!=2:
        done.add(t)
        for u in edges[t]:
            if u==t: continue
            edges[u].remove(t)
            targets.add(u)
        edges[t].clear()
if len(done)==N:
    print("No")
else:
    print("Yes")
