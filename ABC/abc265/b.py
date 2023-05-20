import collections
N,M,T=map(int, input().split())
array=list(map(int, input().split()))
bonus=collections.defaultdict(int)
for _ in range(M):
    x,y=map(int, input().split())
    bonus[x-1]=y
for i in range(N-1):
    T-=array[i]
    if T<=0:
        print("No")
        exit()
    T+=bonus[i+1]
print("Yes")
