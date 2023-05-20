import collections
MOD=998244353
P=int(input())
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
divisors=make_divisors(P-1)
gcd_count=collections.defaultdict(int)
for i in range(len(divisors)-1,-1,-1):
    d1=divisors[i]
    gcd_count[d1]+=(P-1)//d1
    for j in range(i+1,len(divisors)):
        d2=divisors[j]
        if d2%d1==0:
            gcd_count[d1]-=gcd_count[d2]
ret=1 # (0,0)
for gcd in gcd_count:
    c=gcd_count[gcd]
    ret+=((P-1)//gcd)%MOD*c%MOD
    ret%=MOD
print(ret)
