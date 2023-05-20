T=int(input())
for _ in range(T):
    N=input()
    intN=int(N)
    L=len(N)
    ret=int("9"*(L-1))
    for d in range(2,len(N)+1):
        if L%d!=0: continue
        l=L//d
        N0=N[:l]
        r=int(N0*d)
        if r<=intN:
            ret=max(ret,r)
        else:
            N1=str(int(N0)-1)
            if len(N0)==len(N1):
                r=int(N1*d)
                ret=max(ret,r)
    print(ret)
