N=int(input())
if N==1:
    print(1)
    exit()
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
divs=make_divisors(2*N)
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
if N%2==0:
    ret=2*N-1
else:
    ret=N-1
for d1 in divs:
    d2=2*N//d1
    d,x,y=extgcd(d1,d2)
    if d==1 and x!=0 and y!=0:
        r=min(abs(d1*x),abs(d2*y))
        ret=min(ret,r)
print(ret)
