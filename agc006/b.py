N,x=map(int, input().split())
if N==2:
    if x==2:
        print("Yes")
        for a in [1,2,3]:
            print(a)
    else:
        print("No")
else:
    if x==1 or x==2*N-1:
        print("No")
    else:
        print("Yes")
        rets=[i+1 for i in range(2*N-1)]
        rets[x-1],rets[N-1]=rets[N-1],rets[x-1]
        rets[N-2],rets[0]=rets[0],rets[N-2]
        rets[N],rets[-1]=rets[-1],rets[N]
        if x!=2:
            rets[N+1],rets[1]=rets[1],rets[N+1]
        if x!=2*N-2 and N!=4 and N!=3:
            rets[N-3],rets[-2]=rets[-2],rets[N-3]
        for a in rets:
            print(a)
