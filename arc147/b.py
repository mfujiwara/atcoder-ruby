N=int(input())
array=list(map(int, input().split()))
needA=[False]*N
for i,a in enumerate(array):
    if a%2==i%2:
        needA[i]=True
rets=[]
for i in range(2,N):
    if needA[i]:
        k=i-2
        while k>=0 and needA[k]==False:
            rets.append(("B",k+1))
            array[k],array[k+2]=array[k+2],array[k]
            needA[k],needA[k+2]=needA[k+2],needA[k]
            k-=2
#print(array)
for i in range(0,N,2):
    if needA[i]:
        rets.append(("A",i+1))
        array[i],array[i+1]=array[i+1],array[i]
#print(array)
for i in range(N-2):
    for j in range(N-2-i):
        if array[j]>array[j+2]:
            array[j],array[j+2]=array[j+2],array[j]
            rets.append(("B",j+1))
#print(array)
print(len(rets))
for ret in rets:
    print(*ret)
