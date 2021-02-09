N,K=map(int, input().split())
array=list(map(int, input().split()))
brray=[0]*41
base=0
for a in array:
    base+=a
    for i in range(41):
        if a%2==0:
            brray[i]+=1
        else:
            brray[i]-=1
        a//=2
kbits=[]
kbits_1=[]
k=K+1
for i in range(41):
    if k%2==0:
        kbits.append(0)
    else:
        kbits.append(1)
        kbits_1.append(i)
    k//=2
bits=[[] for _ in range(len(kbits_1))]
for i,b in enumerate(kbits_1):
    for j in range(41):
        if j==b:
            bits[i].append(0)
        elif j<b:
            bits[i].append(None)
        else:
            bits[i].append(kbits[j])
ret=0
for bit in bits:
    r=0
    for i,b in enumerate(brray):
        if bit[i]==None:
            if b>0:
                r+=b*2**i
        elif bit[i]==1:
            r+=b*2**i
    ret=max(ret,r)
print(ret+base)
