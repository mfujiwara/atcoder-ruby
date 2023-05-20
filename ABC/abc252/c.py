N=int(input())
rets=[0]*10
counts=[[0]*10 for _ in range(10)]
for _ in range(N):
    array=list(map(int,list(input())))
    for i,a in enumerate(array):
        d=counts[a][i]*10+i
        rets[a]=max(rets[a],d)
        counts[a][i]+=1
    #print(rets)
print(min(rets))
