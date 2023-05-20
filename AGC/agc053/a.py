N=int(input())
s=[0]*(N)
for i,ch in enumerate(input()):
    if ch=="<":
        s[i]=1
    else:
        s[i]=-1
array=list(map(int, input().split()))
left=1
right=max(array)+1
while True:
    if left+1==right:
        break
    mid=(left+right)//2
    rets=[[] for _ in range(mid)]
    for a in array:
        r,q=divmod(a,mid)
        for i in range(mid):
            rets[i].append(r+1 if i<q else r)
    b=True
    for ret in rets:
        for i in range(N):
            if s[i]==1:
                if ret[i]>=ret[i+1]:
                    b=False
                    break
            if s[i]==-1:
                if ret[i]<=ret[i+1]:
                    b=False
                    break
        if not b:
            break
    if b:
        left=mid
    else:
        right=mid    
print(left)
rets=[[] for _ in range(left)]
for a in array:
    r,q=divmod(a,left)
    for i in range(left):
        rets[i].append(r)
        if i<q:
            rets[i][-1]+=1
for ret in rets:
    print(" ".join(map(str,ret)))
