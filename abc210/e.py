import math
N,M=map(int, input().split())
cas=[]
for _ in range(M):
    a,c=map(int, input().split())
    cas.append((c,a))
cas.sort()
group=N
ret=0
for c,a in cas:
    g=math.gcd(group,a)
    if g<group:
        ret+=c*(group-g)
        group=g
        if group==1:
            break
if group==1:
    print(ret)
else:
    print(-1)
