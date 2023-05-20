import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
total=0
for c in counts.values():
    total+=c*(c-1)//2
for a in array:
    c=counts[a]
    ret=total-c*(c-1)//2+(c-1)*(c-2)//2
    print(ret)
