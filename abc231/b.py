import collections
N=int(input())
ret=""
maxi=0
counts=collections.defaultdict(int)
for _ in range(N):
    s=input()
    counts[s]+=1
    if counts[s]>maxi:
        maxi=counts[s]
        ret=s
print(ret)
