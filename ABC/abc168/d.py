N,M=map(int, input().split())
paths=[[] for i in range(N)]
for i in range(M):
    a,b=map(int, input().split())
    paths[a-1].append(b-1)
    paths[b-1].append(a-1)

targets=[0]
rets=[0]*N
rets[0]=-1
while len(targets)>0:
    nexts=[]
    for t in targets:
        for i in paths[t]:
            if rets[i]==0:
                targets.append(i)
                rets[i]=t+1
    targets=nexts
print("Yes")
for i in range(1,N):
    print(rets[i])
