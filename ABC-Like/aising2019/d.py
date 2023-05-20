import bisect
N,Q=map(int, input().split())
array=list(map(int, input().split()))
rets=[sum(array[N//2:])]
ranges=[]
for i in range(N//2):
    j=N//2+i
    k=i*2
    if N%2==0:
        k+=1
    ranges.append((array[j]+array[k])//2+1)
    rets.append(rets[-1]-array[j]+array[k])
for _ in range(Q):
    x=int(input())
    index=bisect.bisect_right(ranges,x)
    print(rets[index])
