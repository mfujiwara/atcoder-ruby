import heapq
Q=int(input())
diff=0
queue=[]
heapq.heapify(queue)
for _ in range(Q):
    q=input()
    if q[0]=="1":
        _,x=q.split()
        x=int(x)
        heapq.heappush(queue,x-diff)
    elif q[0]=="2":
        _,x=q.split()
        x=int(x)
        diff+=x
    else:
        print(heapq.heappop(queue)+diff)
