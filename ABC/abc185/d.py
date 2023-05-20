N,M=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
array=[0]+array+[N+1]
k=N
for i in range(M+1):
    diff=array[i+1]-array[i]-1
    if diff>0:
        k=min(k,diff)
ret=0
for i in range(M+1):
    diff=array[i+1]-array[i]-1
    if diff>0:
        ret+=(diff+k-1)//k
print(ret)
