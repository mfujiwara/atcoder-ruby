import collections
Q=int(input())
queue=collections.deque()
for _ in range(Q):
    query=list(map(int, input().split()))
    if query[0]==1:
        x=query[1]
        c=query[2]
        queue.append((x,c))
    else:
        c=query[1]
        total_c=0
        total_x=0
        while total_c!=c:
            xx,cc=queue.popleft()
            if total_c+cc<=c:
                total_c+=cc
                total_x+=cc*xx
            else:
                back_c=total_c+cc-c
                queue.appendleft((xx,back_c))
                total_c+=(cc-back_c)
                total_x+=(cc-back_c)*xx
        print(total_x)
