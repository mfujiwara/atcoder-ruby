N,M=map(int, input().split())
P=[input() for _ in range(N)]
dp=[bin(i).count("1") for i in range(pow(2,N))]
dp[0]=0
for i in range(N-1):
    for j in range(i+1,N):
        bit=pow(2,i)|pow(2,j)
        dp[bit]=1
        for k in range(M):
            if P[i][k]!="*" and P[j][k]!="*" and P[i][k]!=P[j][k]:
                dp[bit]=2
                break
for bit in range(pow(2,N)):
    pattern1=True
    for i in range(N-1):
        if pow(2,i)&bit==0: continue
        for j in range(i+1,N):
            if pow(2,j)&bit==0: continue
            if dp[pow(2,i)|pow(2,j)]!=1:
                pattern1=False
    if pattern1:
        dp[bit]=1
        continue
    mask=bit
    while bit>0:
        dp[mask]=min(dp[mask],dp[mask-bit]+dp[bit])
        bit=(bit-1)&mask
print(dp[-1])
