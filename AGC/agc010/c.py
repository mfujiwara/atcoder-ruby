N=int(input())
array=list(map(int, input().split()))
edges=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
parents=[-1]*N
status=[0]*N
targets=[0]
while targets:
    #print(targets)
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                parents[u]=t
                targets.append(u)
    else:
        total=0
        subs=[]
        subs_max=0
        for u in edges[t]:
            if parents[t]!=u:
                a=array[u]
                total+=a
                subs.append(a)
                subs_max=max(subs_max,a)
        if len(subs)==0: continue
        # ペアx個
        x=total-array[t]
        # 親につなげるa個
        a=2*array[t]-total
        if a<0 or x<0:
            print("NO")
            exit()
        # tからどこかに繋がる最大パス数
        maxi=max(subs_max,a)
        if maxi>array[t]:
            print("NO")
            exit()        
        array[t]=a
if len(edges[0])>1 and array[0]==0 or len(edges[0])==1:
    print("YES")
else:
    print("NO")
