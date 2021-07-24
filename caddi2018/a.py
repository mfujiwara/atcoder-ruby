def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
import collections
N,P=map(int, input().split())
counts=collections.Counter(prime_factorize(P))
ret=1
for a in counts:
    n=counts[a]
    ret*=pow(a,n//N)
print(ret)
