import math
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
def lcm(a,b):
    return a*b//math.gcd(a,b)
N=int(input())
ab=[]
lcms=[]
for _ in range(N):
    a,b=map(int, input().split())
    ab.append((a,b))
    lcms.append(lcm(a,b))
g=lcms.pop()
while lcms:
    g=math.gcd(g,lcms.pop())
divisors=make_divisors(g)
while divisors:
    d=divisors.pop()
    x=y=d
    valid=True
    for a,b in ab:
        nx=math.gcd(a,x)
        ny=math.gcd(b,y)
        if lcm(nx,ny)==d:
            x=nx
            y=ny
            continue
        nx=math.gcd(a,y)
        ny=math.gcd(b,x)
        if lcm(nx,ny)==d:
            x=nx
            y=ny
            continue
        valid=False
        break
    if valid:
        print(d)
        exit()
