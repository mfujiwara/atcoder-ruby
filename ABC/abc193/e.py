def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
def crt(r, m):
    y,z = 0,1
    for i in range(len(r)):
        d,p,_ = extgcd(z,m[i])
        if (r[i]-y)%d!=0: return (0,-1)
        tmp = (r[i]-y)//d*p%(m[i]//d)
        y+=z*tmp
        z*=m[i]//d
    return (y%z,z)
T=int(input())
for _ in range(T):
    X,Y,P,Q=map(int, input().split())
    # X <= t < X+Y (mod 2X+2Y)
    # P <= t < P+Q (mod P+Q)

    # t=(2X+2Y)n+X+a
    # t=(P+Q)m+P+b
    # (2X+2Y)n-(P+Q)m=P-X+b-a
    d,x,y=extgcd(2*X+2*Y,P+Q)
    ret=-1
    for a in range(0,Y):
        for b in range(0,Q):
            y,z=crt([X+a,P+b],[2*X+2*Y,P+Q])
            if y!=0:
                if ret==-1:
                    ret=y
                else:
                    ret=min(ret,y)
    if ret==-1:
        print("infinity")
    else:
        print(ret)
