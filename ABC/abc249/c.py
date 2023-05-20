import collections
ord_a=ord("a")
N,K=map(int, input().split())
counts=[[0]*26 for _ in range(N)]
for i in range(N):
    s=input()
    for ch in s:
        counts[i][ord(ch)-ord_a]+=1
ret=0
for bit in range(1,pow(2,N)):
    c=[0]*26
    k=0
    while bit>0:
        bit,r=divmod(bit,2)
        if r==1:
            for i in range(26):
                c[i]+=counts[k][i]
        k+=1
    r=0
    for i in range(26):
        if c[i]==K:
            r+=1
    ret=max(ret,r)
print(ret)
