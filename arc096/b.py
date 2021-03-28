N,C=map(int, input().split())
xv=[list(map(int, input().split())) for _ in range(N)]
sums=[0]
returns=[0]
v_sum=0
for x,v in xv:
    v_sum+=v
    sums.append(v_sum-x)
    returns.append(max(returns[-1],v_sum-2*x))
sums_inv=[0]
returns_inv=[0]
v_sum=0
for x,v in xv[::-1]:
    v_sum+=v
    sums_inv.append(v_sum+x-C)
    returns_inv.append(max(returns_inv[-1],v_sum+2*x-2*C))
ret=0
for i,sum in enumerate(sums):
    r=sum+returns_inv[-1-i]
    ret=max(ret,r)
for i,sum in enumerate(sums_inv):
    r=sum+returns[-1-i]
    ret=max(ret,r)
print(ret)
