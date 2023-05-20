N,M=map(int, input().split())
array=list(map(lambda e:int(e)-1, input().split()))
done=[False]*(N+M)
ret=0
stockN=0
stockM=0
for i,a in enumerate(array):
    if i==a or done[i]:
        continue
    single=True
    j=i
    c=1
    while True:
        k=array[j]
        done[k]=True
        if j<N<=i or i<N<=j:
            single=False
        if k==i:
            break
        c+=1
        j=k
    if single:
        if i<N and stockM>0:
            stockM-=1
            ret+=c-1
        elif i>=N and stockN>0:
            stockN-=1
            ret+=c-1
        else:
            if i<N:
                stockN+=1
            else:
                stockM+=1
            ret+=c+1        
    else:
        ret+=c-1
print(ret)
