import heapq
MOD=pow(10,9)+7
N,A,B=map(int, input().split())
array=list(map(int, input().split()))
heapq.heapify(array)
if A==1:
    for _ in range(N):
        a=heapq.heappop(array)
        print(a%MOD)
    exit()    
maxi=max(array)
while B>0 and array[0]<maxi:
    a=heapq.heappop(array)
    a*=A
    heapq.heappush(array,a)
    B-=1
if B==0:
    for i in range(N):
        a=heapq.heappop(array)
        print(a%MOD)    
else:
    q,r=divmod(B,N)
    rets=[0]*N
    for i in range(N):
        a=heapq.heappop(array)
        a%=MOD
        if i<r:
            a=a*A%MOD
        rets[(N-r+i)%N]=a
    for r in rets:
        r*=pow(A,q,MOD)
        r%=MOD
        print(r)
