import collections
MOD=pow(10,9)+7
N=int(input())
edge_list=[]
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
    edge_list.append((a,b))
targets=[(0,0)]
parent=[-2]*N
parent[0]=-1
child_nums=[0]*N
while targets:
    t,s=targets.pop()
    if s==0:
        targets.append((t,1))
        for u in edges[t]:
            if u==parent[t]: continue
            parent[u]=t
            targets.append((u,0))
    else:
        for u in edges[t]:
            if u==parent[t]: continue
            child_nums[t]+=child_nums[u]+1
pow2=[1]
inv_pow2=[1]
inv2=MOD - 1 * (MOD // 2) % MOD
for _ in range(N+1):
    pow2.append(pow2[-1]*2%MOD)
    inv_pow2.append(inv_pow2[-1]*inv2%MOD)
s_count=(1-inv_pow2[N])%MOD # 空グラフのとき以外だけ+1
for n1,n2 in edge_list:
    c1=child_nums[n1]
    c2=child_nums[n2]
    x1=min(c1,c2)+1
    x2=N-x1
    #print("x1,x2",x1,x2)
    r1=(pow2[x1]-1)*inv_pow2[x1]%MOD
    r2=(pow2[x2]-1)*inv_pow2[x2]%MOD
    s_count+=r1*r2%MOD
    s_count%=MOD
ret=(s_count-N*inv2)%MOD
print(ret)
