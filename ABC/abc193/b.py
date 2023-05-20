N=int(input())
ret=10**10
for _ in range(N):
    a,p,x=map(int, input().split())
    if a<x:
        ret=min(ret,p)
if ret<10**10:
    print(ret)
else:
    print(-1)
