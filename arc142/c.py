N=int(input())
ret=N
d12=None
d21=None
for n in range(3,N+1):
    print("?",1,n,flush=True)
    d1=int(input())
    print("?",2,n,flush=True)
    d2=int(input())
    ret=min(ret,d1+d2)
    if d1==1 and d2==2:
        d12=n
    elif d1==2 and d2==1:
        d21=n
if ret!=3:
    print("!",ret)
else:
    if d12==None or d21==None:
        print("!",1)
    else:
        print("?",d12,d21,flush=True)
        d=int(input())
        if d==1:
            print("!",3)
        else:
            print("!",1)