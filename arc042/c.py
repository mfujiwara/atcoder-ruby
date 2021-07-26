import collections
N,P=map(int, input().split())
abs=[]
for _ in range(N):
    a,b=map(int, input().split())
    abs.append((a,b))
abs.sort()
ret=0
dp=[-1]*max(abs[-1][0]+1,2*P+1)
dp[0]=0
while abs:
    a,b=abs.pop()
    for a_sum in range(P,-1,-1):
        b_sum=dp[a_sum]
        if b_sum==-1: continue
        if dp[a_sum+a]<b_sum+b:
            dp[a_sum+a]=b_sum+b
            ret=max(ret,b_sum+b)
print(ret)
