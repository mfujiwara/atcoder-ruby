N=int(input())
A=int(input())
a_array=[]
for _ in range(A):
    x,y=map(int, input().split())
    a_array.append((x-1, y-1))
B=int(input())
b_array=[]
for _ in range(B):
    x,y=map(int, input().split())
    b_array.append((x-1, y-1))
ret=0
for bit in range(pow(2,B)):
    # 塗らない集合について全通り試す
    ng_set=set()
    for i in range(B):
        if bit >> i & 1:
            ng_set.add(b_array[i][0])
    # enable[i]:=iが塗られた時に塗れる点一覧
    enable=[[] for _ in range(N)]
    # stopper[i]:=iを塗れるまでに必要な塗られるべき他の点の数
    stopper=[0]*N
    done=[False]*N
    for x,y in a_array:
        enable[y].append(x)
        stopper[x]+=1
    for x,y in b_array:
        if x not in ng_set:
            enable[x].append(y)
            stopper[y]+=1
    r=0
    while True:
        pre_r=r
        for i in range(N):
            if i in ng_set: continue
            if stopper[i]==0 and not done[i]:
                r+=1
                done[i]=True
                for k in enable[i]:
                    stopper[k]-=1
        if pre_r==r:
            break
    ret=max(ret,r)
print(ret)
