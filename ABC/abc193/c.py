N=int(input())
primes=[2,3,5,7,11,13,17,19,23,29,31]
memo=set()
for p in primes:
    for n in range(2,N):
        value=n**p
        if value<=N:
            memo.add(value)
        else:
            break
print(N-len(list(memo)))
