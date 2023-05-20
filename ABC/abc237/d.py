import collections
N=int(input())
S=input()
queue=collections.deque([N])
for i in range(N-1,-1,-1):
    ch=S[i]
    if ch=="L":
        queue.append(i)
    else:
        queue.appendleft(i)
print(*queue)
