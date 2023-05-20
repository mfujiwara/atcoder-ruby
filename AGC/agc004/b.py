N,x=map(int, input().split())
array=list(map(int, input().split()))
starts=array[:]
total=sum(array)
ret=total
for i in range(1,N):
    updates={}
    for j in range(N):
        if array[j]>starts[(j-i+N)%N]:
            updates[j]=array[j]-starts[(j-i+N)%N]
    for j in updates:
        total-=updates[j]
        array[j]-=updates[j]
    v=total+x*i
    ret=min(ret,v)
print(ret)
