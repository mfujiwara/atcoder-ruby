import math
N=map(int, input().split())
array=list(map(int, input().split()))
def prime_factorize(n):
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return list(a)
rets=[1]
for a in array:
    primes=prime_factorize(a)
    for i in range(len(rets)):
        ret=rets[i]
        if math.gcd(ret,a)==1:
            for j in range(len(primes)):
                if j==0:
                    rets[i]*=primes[j]
                else:
                    rets.append(ret*primes[j])
print(min(rets))
