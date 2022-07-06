N,K=map(int, input().split())
if K>int(str(K)[::-1]):
    print(0)
elif K%10!=0:
    ret=0
    k=K
    while N>=k:
        ret+=1
        k*=10
    l=int(str(K)[::-1])
    if K!=l:
        while N>=l:
            ret+=1
            l*=10
    print(ret)
else:
    print(0)
