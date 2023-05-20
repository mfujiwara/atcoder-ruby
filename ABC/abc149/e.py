import itertools
N,M=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
sums=list(itertools.accumulate(array))
left=0
right=array[-1]*2+1
while left+1!=right:
    mid=(left+right)//2
    ret=0
    i=N
    for a in array:
        while i>0 and a+array[i-1]>=mid:
            i-=1
        ret+=i
        if i==0:
            break
    if ret<N*N-M:
        left=mid
    else:
        right=mid
i=0
count=0
ret=0
for a in array[::-1]:
    while i<N and a+array[i]<right:
        i+=1
    if i==N:
        break
    count+=N-i
    ret+=a*(N-i)
    ret+=sums[-1]
    if i>0:
        ret-=sums[i-1]
if count<M:
    ret+=left*(M-count)
print(ret)
