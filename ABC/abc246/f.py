import itertools
MOD=998244353
N,L=map(int, input().split())
bits=[]
ord_a=ord("a")
for _ in range(N):
    s=input()
    bit=0
    for ch in s:
        bit|=1<<(ord(ch)-ord_a)
    bits.append(bit)
ret=0
for r in range(1,N+1):
    for combi in itertools.combinations(bits,r):
        bit=pow(2,26)-1
        for b in combi:
            bit&=b
        c=bin(bit).count("1")
        if r%2==1:
            ret+=pow(c,L,MOD)
            ret%=MOD
        else:
            ret-=pow(c,L,MOD)
            ret%=MOD
print(ret)
