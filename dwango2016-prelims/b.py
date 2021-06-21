N=int(input())
array=list(map(int, input().split()))
rets=[-1]*N
rets[0]=array[0]
rets[-1]=array[-1]
for i in range(1,N-1):
    if array[i-1]<=array[i]:
        rets[i]=array[i-1]
    elif array[i-1]>array[i]:
        rets[i]=array[i]
print(" ".join(map(str,rets)))
