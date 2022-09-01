N=int(input())
array0=list(map(int, input().split()))
array=array0[:]
rets=[]
for i in range(2*N-1):
    if i%2==0:
        if array[i]>array[i+1]:
            if i+2<2*N and array[i]<array[i+2]:
                rets.append(i+2)
                array[i+2],array[i+1]=array[i+1],array[i+2]
            else:
                rets.append(i+1)
                array[i],array[i+1]=array[i+1],array[i]
    else:
        if array[i]<array[i+1]:
            if i+2<2*N and array[i]>array[i+2]:
                rets.append(i+2)
                array[i+2],array[i+1]=array[i+1],array[i+2]
            else:
                rets.append(i+1)
                array[i],array[i+1]=array[i+1],array[i]
print(len(rets))
print(*rets)
