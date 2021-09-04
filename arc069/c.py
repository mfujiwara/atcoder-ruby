N=int(input())
array=list(map(int, input().split()))
total=sum(array)
array=[(a,i) for i,a in enumerate(array)]
array.sort(key=lambda e: (-e[0],-e[1]))
rets=[0]*N
priority=N
for i,aa in enumerate(array):
    a,index=aa
    priority=min(priority,index)
    if index==0:
        rets[0]+=total
        break
    diff=a-array[i+1][0]
    v=diff*(i+1)
    rets[priority]+=v
    total-=v
for r in rets:
    print(r)
