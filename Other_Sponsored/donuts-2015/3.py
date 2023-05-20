import bisect
import collections
N=int(input())
array=list(map(int, input().split()))
stack=collections.deque([])
ignore=0
for a in array:
    print(len(stack)-ignore)
    i=bisect.bisect_right(stack,a)
    for _ in range(i):
        stack.popleft()
    stack.appendleft(a)
