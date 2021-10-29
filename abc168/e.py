import collections
import math
MOD=pow(10,9)+7
N=int(input())
zero=0
counts1=collections.defaultdict(int)
counts2=collections.defaultdict(int)
for _ in range(N):
    a,b=map(int, input().split())
    if a==0 and b==0:
        zero+=1
        continue
    if a==0:
        g=b
    elif b==0:
        g=a
    else:
        g=math.gcd(a,b)
    a//=g
    b//=g
    if b<0:
        a*=-1
        b*=-1
    if a>0:
        counts1[(a,b)]+=1
        counts2[(-b,a)]+=0
    else:
        counts2[(a,b)]+=1
        counts1[(b,-a)]+=0
ret=1
for key1 in counts1:
    key2=(-key1[1],key1[0])
    ret*=(pow(2,counts1[key1],MOD)+pow(2,counts2[key2],MOD)-1)
    ret%=MOD
print((ret-1+zero)%MOD)
