import math
T=int(input())
dp=[0,1]
sums=[0,1]
INF=int(math.sqrt(math.sqrt(9*pow(10,18))))+1
for i in range(len(dp),INF):
    j=int(math.sqrt(i))
    dp.append(sums[j])
    sums.append(sums[-1]+dp[-1])
for _ in range(T):
    X=int(input())
    x2=int(math.sqrt(X))
    while x2**2>X:
        x2-=1
    while (x2+1)**2<=X:
        x2+=1
    x=int(math.sqrt(x2))
    while x**2>x2:
        x-=1
    while (x+1)**2<=x2:
        x+=1
    ret=0
    for i in range(1,x+1):
        ret+=dp[i]*(x2-i*i+1)
    print(ret)
