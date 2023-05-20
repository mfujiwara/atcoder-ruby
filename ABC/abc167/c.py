N,M,X=map(int, input().split())
CA=[list(map(int, input().split())) for _ in range(N)]
ret=-1
for i in range(1,pow(2,N)):
    k=0
    a_total=[0]*M
    c_total=0
    while i>0:
        i,r=divmod(i,2)    
        if r==1:
            array=CA[k]
            c_total+=array[0]
            array=array[1:]
            for j,a in enumerate(array):
                a_total[j]+=a
        k+=1
    judge=True
    for j in range(M):
        if a_total[j]<X:
            judge=False
            break
    if judge:
        if ret==-1:
            ret=c_total
        else:
            ret=min(ret,c_total)
print(ret)
