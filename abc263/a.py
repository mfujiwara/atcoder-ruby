import collections


array=map(int, input().split())
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
values=list(counts.values())
if values==[2,3] or values==[3,2]:
    print("Yes")
else:
    print("No")
