import collections
N,Q=map(int, input().split())
array=collections.deque(list(map(int, input().split())))
for _ in range(Q):
    t,x,y=map(int, input().split())
    if t==1:
        array[x-1],array[y-1]=array[y-1],array[x-1]
    elif t==2:
        a=array.pop()
        array.appendleft(a)
    else:
        print(array[x-1])
