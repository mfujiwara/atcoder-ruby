import collections
MOD=pow(10,9)+7
def prime_factorize(n):
    a = collections.defaultdict(int)
    while n % 2 == 0:
        a[2]+=1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f]+=1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n]+=1
    return a
N,M=map(int, input().split())
primes=prime_factorize(abs(N))
primes[0]
maxi=max(primes.values())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,M+maxi):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
ret=1
for key,val in primes.items():
    ret*=fn[val+M-1]
    ret%=MOD
    ret*=fn_inv[M-1]
    ret%=MOD
    ret*=fn_inv[val]
    ret%=MOD
ret*=pow(2,M-1,MOD)
ret%=MOD
print(ret)
