N=input()
if len(N)%2==0:
    a=int(N[:len(N)//2])
    b=int(N[len(N)//2:])
    if a<=b:
        print(a)
    else:
        print(a-1)
else:
    k=(len(N)-1)//2
    print(10**k-1)
