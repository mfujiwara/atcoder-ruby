L,N=map(int, input().split())
array=[0]*N
sums=[0]*N
total=0
for i in range(N):
    x=int(input())
    array[i]=x
    total+=x
    sums[i]=total
total=0
inv=[0]*N
inv_sums=[0]*N
for i in range(N):
    x=L-array[-1-i]
    inv[i]=x
    total+=x
    inv_sums[i]=total
if N==1:
    print(max(array[0],inv[0]))
    exit()
ret=0
for i in range(1,N):
    rr=array[i-1]*2
    x=(N-i)//2
    y=N-i-x
    rr+=(sums[i-1+x]-sums[i-1])*2
    rr+=inv_sums[y-1]*2
    if x==y:
        rr-=array[i-1+x]
    else:
        rr-=inv[y-1]
    ret=max(ret,rr)
for i in range(1,N):
    rr=inv[i-1]*2
    x=(N-i)//2
    y=N-i-x
    rr+=(inv_sums[i-1+x]-inv_sums[i-1])*2
    rr+=sums[y-1]*2
    if x==y:
        rr-=inv[i-1+x]
    else:
        rr-=array[y-1]
    ret=max(ret,rr)
print(ret)
# print(array,sums)
# print(inv,inv_sums)
