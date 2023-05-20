import heapq
N=int(input())
array=list(map(int, input().split()))
sub1=[]
sub2=[]
for i in range(N):
    sub1.append(array[i])
    sub2.append(-array[-N+i])
heapq.heapify(sub1)
heapq.heapify(sub2)
h1=[0]*(N+1)
h2=[0]*(N+1)
h1[0]=sum(sub1)
h2[-1]=sum(sub2)
for i in range(1,N+1):
    heapq.heappush(sub1,array[N-1+i])
    d=heapq.heappop(sub1)
    h1[i]+=(h1[i-1]+array[N-1+i]-d)
    heapq.heappush(sub2,-array[-N-i])
    d=heapq.heappop(sub2)
    h2[-1-i]+=(h2[-i]-array[-N-i]-d)
ret=h1[0]+h2[0]
for i in range(1,N+1):
    ret=max(ret,h1[i]+h2[i])
print(ret)
