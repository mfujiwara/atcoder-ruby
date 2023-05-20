import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    edges[b].append(a)
s=input()
group=""
calls=[]
op=False
for ch in s:
    if "0"<=ch<="9":
        group+=ch
    elif ch=="w":
        op=True
    elif len(group)>0 and ch=="\"":
        calls.append(op)
        op=False
calls.append(op)
group=int(group)
targets=set([group])
for op in calls:
    if op:
        nexts=set()
        for t in targets:
            for u in edges[t]:
                nexts.add(u)
        targets=nexts
    else:
        nexts=None
        for t in targets:
            if nexts==None:
                nexts=set(edges[t])
            else:
                nexts&=set(edges[t])
        targets=[i+1 for i in range(N) if i+1 not in nexts]
print(len(targets))
