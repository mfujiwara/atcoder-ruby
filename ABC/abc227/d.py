import heapq
from itertools import count
N,K=map(int, input().split())
array=list(map(int, input().split()))
array.sort(reverse=True)
left=0
right=pow(10,18)
while left+1<right:
    mid=(left+right)//2
    counts=[mid]*K
    for a in array:
        if len(counts)==0:
            break
        if a<counts[-1]:
            counts[-1]-=a
        elif len(counts)==1:
            counts.pop()
        elif a>=mid:
            counts[-2]=counts[-1]
            counts.pop()
        else:
            a-=counts[-1]
            counts.pop()
            counts[-1]-=a
    if len(counts)==0:
        left=mid
    else:
        right=mid
print(left)
