import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
ret=0
for key in counts:
    c=counts[key]
    if c>=key:
        ret+=c-key
    else:
        ret+=c
print(ret)
