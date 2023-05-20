import collections
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
N=int(input())
counts = collections.Counter(prime_factorize(N))
memo=collections.defaultdict(int)
ret=0
for key in counts:
    num=counts[key]
    c=1
    while num>=c:
        num-=c
        c+=1
        ret+=1
print(ret)
