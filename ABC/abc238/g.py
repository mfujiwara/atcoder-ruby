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
MOD=pow(10,9)+7
N,Q=map(int, input().split())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
memo=[1]
hash=1
for a in array:
    for f in prime_factorize(a):
        hash*=f
        hash%=MOD
        counts[f]+=1
        if counts[f]==3:
            hash*=pow(f,3*(MOD-2),MOD)
            hash%=MOD
            counts[f]=0
    memo.append(hash)
for _ in range(Q):
    l,r=map(int, input().split())
    if memo[l-1]==memo[r]:
        print("Yes")
    else:
        print("No")
