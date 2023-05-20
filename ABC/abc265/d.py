import itertools
N,P,Q,R=map(int, input().split())
array=list(map(int, input().split()))
sums=list(itertools.accumulate(array))
sums_index={}
for i in range(N):
    sums_index[sums[i]]=i
if P in sums_index:
    t=sums_index[P]
    v=sums[t]
    if v+Q in sums_index:
        t=sums_index[v+Q]
        v=sums[t]
        if v+R in sums_index:
            print("Yes")
            exit()
for i in range(N):
    v=sums[i]
    if v+P in sums_index:
        t=sums_index[v+P]
        v=sums[t]
        if v+Q in sums_index:
            t=sums_index[v+Q]
            v=sums[t]
            if v+R in sums_index:
                print("Yes")
                exit()
print("No")
