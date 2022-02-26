A,B=map(int, input().split())
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
single_bits={}
for i,p in enumerate(primes):
    single_bits[p]=pow(2,i)
prime_bits={}
for x in range(A,B+1):
    bits=0
    for d in primes:
        if x%d==0:
            bits|=single_bits[d]
    prime_bits[x]=bits
dp={} # dp[j]:= 選ばれてない素数bitがj
dp[pow(2,len(primes))-1]=1
for x in range(A,B+1):
    nexts={}
    for bit in list(dp.keys()):
        if bit in nexts:
            nexts[bit]+=dp[bit]
        else:
            nexts[bit]=dp[bit]
        if bit|prime_bits[x]==bit:
            new_bit=bit^prime_bits[x]
            if new_bit in nexts:
                nexts[new_bit]+=dp[bit]
            else:
                nexts[new_bit]=dp[bit]
    dp=nexts
print(sum(dp.values()))
