import collections
n=int(input())
array=list(map(int, input().split()))
rets=collections.deque([])
for i,a in enumerate(array):
    if i%2==0:
        rets.append(a)
    else:
        rets.appendleft(a)
if n%2==0:
    print(*rets)
else:
    print(*list(rets)[::-1])
