import collections


N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
array.sort()
ret=0
while array:
    n=array.pop()
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i != n // i:
                j=n//i
                ret+=counts[i]*counts[j]*2
            else:
                ret+=counts[i]*counts[i]
        i += 1
print(ret)
