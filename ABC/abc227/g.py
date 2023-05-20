import collections
def primes(nn):
    is_prime = [True] * nn
    is_prime[0] = is_prime[1] = False
    for p in range(2, nn):
        if not is_prime[p]:
            continue
        for q in range(p ** 2, nn, p):
            is_prime[q] = False
    primes = [p for p in range(2, nn) if is_prime[p]]
    return primes
MOD=998244353
N,K=map(int, input().split())
if K==0:
    print(1)
    exit()
counts=collections.defaultdict(int)
array1=[N-K+1+i for i in range(K)]
array2=[i+1 for i in range(K)]
for p in primes(pow(10,6)+1):
    r=(N-K+1)%p
    index=0 if r==0 else p-r
    while index<len(array1):
        if array1[index]%p==0:
            array1[index]//=p
            counts[p]+=1
        else:
            index+=p
    r=array2[0]%p
    index=0 if r==0 else p-r
    while index<len(array2):
        if array2[index]%p==0:
            array2[index]//=p
            counts[p]-=1
        else:
            index+=p
# print(array1)
# print(array2)
# print(counts)
ret=1
for v in counts.values():
    ret*=(v+1)
    ret%=MOD
for a in array1:
    if a!=1:
        ret*=2
        ret%=MOD
print(ret)
