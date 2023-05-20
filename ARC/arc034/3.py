from collections import defaultdict
MOD=10**9+7
def prime_factorize(n,dic):
    while n % 2 == 0:
        dic[2]+=1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            dic[f]+=1
            n //= f
        else:
            f += 2
    if n != 1:
        dic[n]+=1
A,B=map(int, input().split())
dic=defaultdict(int)
for n in range(B+1,A+1):
    prime_factorize(n, dic)
ret=1
for key in dic:
    if key!=1:
        ret*=(dic[key]+1)
        ret%=MOD
print(ret)
