N,Q=map(int, input().split())
array=list(map(int, input().split()))
diffs=[]
total=0
for i in range(N-1):
    diffs.append(array[i+1]-array[i])
    total+=abs(array[i+1]-array[i])
rets=[]
for _ in range(Q):
    l,r,v=map(int, input().split())
    if l>1:
        nl=diffs[l-2]+v
        total+=abs(nl)-abs(diffs[l-2])
        diffs[l-2]=nl
    if r<N:
        nr=diffs[r-1]-v
        total+=abs(nr)-abs(diffs[r-1])
        diffs[r-1]=nr
    print(total)
