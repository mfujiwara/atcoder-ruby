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
N=int(input())
array=list(map(int, input().split()))
mini=min(array)
memo={}
for a in array:
    divs=make_divisors(a)
    for d in divs:
        if d>mini: break
        if d in memo:
            memo[d]=math.gcd(memo[d],a//d)
        else:
            memo[d]=a//d
ret=sum([1 for v in memo.values() if v==1])
print(ret)
