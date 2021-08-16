N=int(input())
lrs=[]
max_l=0
min_r=10**9
max_size=0
for _ in range(N):
    l,r=map(int, input().split())
    lrs.append((l,r))
    max_l=max(max_l,l)
    min_r=min(min_r,r)
    max_size=max(max_size,r-l+1)
ret=max(min_r-max_l+1,0)+max_size
abs=[]
for l,r in lrs:
    abs.append((max(r-max_l+1,0),max(min_r-l+1,0)))
abs.sort()
aaa=[10**9]
bbb=[10**9]
for i in range(N-1,-1,-1):
    a,_=abs[i]
    aaa.append(min(aaa[-1],a))
for i in range(N):
    _,b=abs[i]
    bbb.append(min(bbb[-1],b))
bbb=bbb[::-1]
for i in range(1,N):
    ret=max(ret,aaa[i]+bbb[i])
print(ret)
