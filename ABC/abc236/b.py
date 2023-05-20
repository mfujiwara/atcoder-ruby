import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
for c in counts:
    if counts[c]==3:
        print(c)
        exit()
