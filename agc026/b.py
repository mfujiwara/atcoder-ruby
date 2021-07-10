def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
T=int(input())
rets=[]
for _ in range(T):
    A,B,C,D=map(int, input().split())
    if A<B or B>D:
        rets.append("No")
        continue
    if B<=C+1:
        rets.append("Yes")
        continue
    # C < A-B*x+D*y < B
    d,x,y=extgcd(B,D)
    # C < A-d*z < B
    # A-B < d*z < A-C
    done=False
    for i in range((A-B)//d,(A-C)//d+1):
        if A-B < d*i < A-C:
            rets.append("No")
            done=True
            break
    if not done:
        rets.append("Yes")
for r in rets:
    print(r)
