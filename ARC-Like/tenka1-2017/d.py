N,K=map(int, input().split())
def create_bits(v):
    bits=[0]*30
    k=0
    while v>0:
        v,r=divmod(v,2)
        if r==1:
            bits[k]=1
        k+=1
    return bits
k_bits=create_bits(K)
abs=[]
ret=0
for _ in range(N):
    a,b=map(int, input().split())
    abs.append((a,b))
    if K|a==K:
        ret+=b
for i in range(30):
    if k_bits[i]==0: continue
    bb=1<<i
    k=(K^bb)|(bb-1)
    r=0
    for a,b in abs:
        if k|a==k:
            r+=b
    ret=max(ret,r)
print(ret)
