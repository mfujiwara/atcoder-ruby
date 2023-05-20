import collections
N,M,Y,Z=map(int, input().split())
c2bit={}
bit2p={}
for i in range(M):
    c,p=input().split()
    bit=pow(2,i)
    c2bit[c]=bit
    bit2p[bit]=int(p)
B=input()
dp=collections.defaultdict(lambda: -pow(10,10))
dp[(0,0)]=0
for b in B:
    nexts=collections.defaultdict(lambda: -pow(10,10))
    bit=c2bit[b]
    p=bit2p[bit]
    for bits,last in dp:
        if last==bit:
            nexts[(bits,last)]=max(nexts[(bits,last)],dp[(bits,last)]+p+Y)
        else:
            nbits=bits|bit
            nexts[(nbits,bit)]=max(nexts[(nbits,bit)],dp[(bits,last)]+p)
        nexts[(bits,last)]=max(nexts[(bits,last)],dp[(bits,last)])
    dp=nexts
ret=0
for key in dp:
    bits,_=key
    v=dp[key]
    if bits==pow(2,M)-1:
        v+=Z
    ret=max(ret,v)
print(ret)
