import heapq
N,X=map(int, input().split())
ta=[]
t_array=list(map(int, input().split()))
a_array=list(map(int, input().split()))
for i in range(N):
    ta.append((t_array[i],a_array[i]))
ta.sort()
at=[]
time=pow(10,5)+1
queue=[]
while time>0:
    while ta and ta[-1][0]==time:
        t,a=ta.pop()
        heapq.heappush(queue,(-a,-t))
    if len(queue)>0:
        a,t=heapq.heappop(queue)
        a=-a
        at.append((a,time))
    time-=1
at.sort()
time=1
total=0
while at:
    a,t=at.pop()
    total+=a
    if total>=X:
        print(time)
        exit()
    time+=1
print(-1)
