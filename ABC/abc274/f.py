import collections
N,A=map(int, input().split())
WXV=[]
for _ in range(N):
    w,x,v=map(int, input().split())
    WXV.append((w,x,v))
ret=0
delta=0.0000001
for i in range(N):
    w,x,v=WXV[i]
    memo=collections.defaultdict(int)
    for j in range(N):
        wj,xj,vj=WXV[j]
        vj-=v
        if vj>0:
            t0=(x-xj)/vj
            t1=(x+A-xj)/vj
            if t0>=0 and t1>=0:
                memo[t0]+=wj
                memo[t1+delta]-=wj
            if t0<0 and t1>=0:
                memo[0]+=wj
                memo[t1+delta]-=wj
        elif vj<0:
            t0=(x+A-xj)/vj
            t1=(x-xj)/vj
            if t0>=0 and t1>=0:
                memo[t0]+=wj
                memo[t1+delta]-=wj
            if t0<0 and t1>=0:
                memo[0]+=wj
                memo[t1+delta]-=wj
        else:
            if x<=xj<=x+A:
                memo[0]+=wj
    keys=sorted(memo.keys())
    total=0
    for k in keys:
        total+=memo[k]
        ret=max(ret,total)
print(ret)
