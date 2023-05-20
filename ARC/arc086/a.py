import collections
N,K=map(int, input().split())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
counts=[(c,a)  for a,c in counts.items()]
counts.sort(reverse=True)
ret=0
while len(counts)>K:
    c,_=counts.pop()
    ret+=c
print(ret)
