import collections
N,M=map(int, input().split())
xyz=collections.defaultdict(list)
for _ in range(M):
    x,y,z=map(int, input().split())
    xyz[x].append((y,z))
targets=collections.defaultdict(int)
targets[0]=1
for i in range(N):
    nexts=collections.defaultdict(int)
    for t in targets:
        for k in range(N):
            bit=pow(2,k)
            if t&bit==0:
                u=t|bit
                nexts[u]+=targets[t]
    removes=set()
    for y,z in xyz[i+1]:
        mask=pow(2,y)-1
        for t in nexts:
            if bin(t&mask).count("1")>z:
                removes.add(t)
    for t in removes:
        nexts.pop(t)
    targets=nexts
print(targets[pow(2,N)-1])
