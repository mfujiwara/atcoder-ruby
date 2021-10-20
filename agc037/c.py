import heapq
N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
queue=[]
for i in range(N):
    if b_array[i]>a_array[i]:
        heapq.heappush(queue,(-b_array[i],i))
    elif a_array[i]>b_array[i]:
        print(-1)
        exit()
ret=0
while queue:
    b,i=heapq.heappop(queue)
    b=-b
    a=b_array[(i+1)%N]
    c=b_array[(i-1+N)%N]
    diff=a+c
    if b<=diff:
        print(-1)
        exit()
    # A[i]<=b-diff*n
    n=(b-a_array[i])//diff
    b_array[i]-=n*diff
    ret+=n
    if b_array[i]>a_array[i]:
        heapq.heappush(queue,(-b_array[i],i))
if ret==0:
    print(-1)
else:
    print(ret)
