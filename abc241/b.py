import collections
N,M=map(int, input().split())
a_array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in a_array:
    counts[a]+=1
b_array=list(map(int, input().split()))
for b in b_array:
    counts[b]-=1
    if counts[b]<0:
        print("No")
        exit()
print("Yes")
