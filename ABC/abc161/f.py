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
ret=len(make_divisors(N-1))-1
for d in make_divisors(N):
    if d<2: continue
    n=N//d
    while n%d==0:
        n//=d
    if n%d==1:
        ret+=1
print(ret)
