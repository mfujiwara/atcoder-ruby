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
N,M=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
divs=set()
while array:
    a=array.pop()
    if a in divs: continue
    d=set(make_divisors(a))
    divs|=d
divs=sorted(list(divs))
memo=[True]*(M+1)
for i in range(1,len(divs)):
    d=divs[i]
    if d>M: break
    if not memo[d]: continue
    k=d
    while k<=M:
        memo[k]=False
        k+=d
rets=[]
for i in range(1,M+1):
    if memo[i]:
        rets.append(i)
print(len(rets))
for r in rets:
    print(r)
