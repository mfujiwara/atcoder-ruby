import collections
N=int(input())
d_array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for d in d_array:
    counts[d]+=1
M=int(input())
t_array=list(map(int, input().split()))
for t in t_array:
    counts[t]-=1
    if counts[t]<0:
        print("NO")
        exit()
print("YES")
