from collections import deque
import collections
N=int(input())
array=list(map(int, input().split()))
array=sorted(set(array))
now=0
stock=N-len(array)
array=collections.deque(array)
while array:
    if array[0]==now+1:
        array.popleft()
        now+=1
    elif array[0]<=now:
        array.popleft()
        stock+=1
    elif stock>=2:
        stock-=2
        now+=1
    else:
        array.pop()
        stock+=1
print(now+stock//2)
