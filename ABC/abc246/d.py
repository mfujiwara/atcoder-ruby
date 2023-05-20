N=int(input())
if N==0:
    print(0)
    exit()
ret=pow(10,18)
for a in range(0,pow(10,6)):
    ng=0
    ok=pow(10,6)
    def check(b):
        v=a*(a*(a+b)+pow(b,2))+pow(b,3)
        return v>=N
    while ng+1!=ok:
        mid=(ok+ng)//2
        if check(mid):
            ok=mid
        else:
            ng=mid
    b=ok
    ret=min(ret,a*(a*(a+b)+pow(b,2))+pow(b,3))
    if a>b:
        break
print(ret)
