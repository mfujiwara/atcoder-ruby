N,K=map(int, input().split())
array=list(map(lambda e: int(e)-1, input().split()))
children=[[] for _ in range(N)]
for i in range(1,N):
    children[array[i]].append(i)
heights=[0]*N
targets=[(0,0)]
ret=0 if array[0]==0 else 1
array[0]=0
while targets:
    t,status=targets.pop()
    if status==0:
        targets.append((t,1))
        for u in children[t]:
            targets.append((u,0))
    else:
        if children[t]:
            h=max([heights[u] for u in children[t]])+1
        else:
            h=0
        if  h==K-1 and array[t]!=0:
            heights[t]=-1
            ret+=1
        else:
            heights[t]=h
print(ret)
