from collections import defaultdict
N=int(input())
array=list(map(int, input().split()))
diffs=defaultdict(int)
base=0
for i,a in enumerate(array):
    if i%2==0:
        base+=a
        diffs[base]+=1
    else:
        base-=a
        diffs[base]+=1
ret=diffs[0]
base=0
for i,a in enumerate(array):
    if i%2==0:
        base+=a
        diffs[base]-=1
    else:
        base-=a
        diffs[base]-=1
    ret+=diffs[base]
print(ret)
