import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
total=0
for a in array:
    total+=a
    counts[a]+=1
Q=int(input())
for _ in range(Q):
    b,c=map(int, input().split())
    k=counts[b]
    counts[b]=0
    counts[c]+=k
    total+=(c-b)*k
    print(total)
