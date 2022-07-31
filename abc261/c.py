import collections
N=int(input())
counts=collections.defaultdict(int)
for _ in range(N):
    s=input()
    if counts[s]==0:
        print(s)
    else:
        print(s+"("+str(counts[s])+")")
    counts[s]+=1
