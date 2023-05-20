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
ret=0
for i in range(1,N+1):
    min_j=1
    for p in prime_factorize(i):
        if min_j%p==0:
            min_j//=p
        else:
            min_j*=p
    # i*min_j * x^2 は平方数
    # min_j*x^2<=N
    if N<min_j:
        continue
    x=int(pow(N/min_j,0.5))
    ret+=x
print(ret)
