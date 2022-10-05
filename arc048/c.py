import math
MOD=pow(10,9)+7
N=int(input())
array=[int(input()) for _ in range(N)]
mini=min(array)
ret=pow(2,mini,MOD)
#print("ret1",ret)
g=0
for a in array:
    if a==mini:
        continue
    g=math.gcd(g,a-mini)
#print("g",g)
ret*=pow(2,(g+1)//2,MOD)%MOD
ret%=MOD
print(ret)
