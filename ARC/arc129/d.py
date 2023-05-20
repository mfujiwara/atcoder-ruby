N=int(input())
array=list(map(int, input().split()))
if sum(array)!=0:
    print(-1)
    exit()
b_array=[0]*N
for i in range(1,N):
    b_array[i]=array[i]+b_array[i-1]
if sum(b_array)%N!=0:
    print(-1)
    exit()
d=sum(b_array)//N
b_array=[b-d for b in b_array]
mini=0
rets=[0]*N
for i in range(1,N):
    rets[i]=b_array[i-1]+rets[i-1]
    mini=min(mini,rets[i])
ret=sum(rets)-mini*N
print(ret)
