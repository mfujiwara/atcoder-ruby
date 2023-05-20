import collections
N=int(input())
jisho=[]
starts=collections.defaultdict(list)
ends=collections.defaultdict(list)
undtermins=collections.defaultdict(set)
for i in range(N):
    s=input()
    start=s[:3]
    end=s[-3:]
    jisho.append((start,end))
    starts[start].append(i)
    ends[end].append(i)
    undtermins[start].add(i)
rets=[0]*N
targets=[]
for i in range(N):
    start,end=jisho[i]
    if len(starts[end])==0:
        targets.append(i)
        rets[i]=1
while targets:
    #print(f"{targets}: {judge}")
    t=targets.pop()
    start,end=jisho[t]
    undtermins[start].remove(t)
    if rets[t]==1:
        for u in ends[start]:
            if rets[u]==0:
                targets.append(u)

                rets[u]=-1
    elif len(undtermins[start])==0:
        for u in ends[start]:
            if rets[u]==0:
                targets.append(u)
                rets[u]=1

for ret in rets:
    if ret==1:
        print("Takahashi")
    elif ret==-1:
        print("Aoki")
    else:
        print("Draw")
