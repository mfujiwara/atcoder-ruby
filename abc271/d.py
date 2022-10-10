N,S=map(int, input().split())
dp=[[""]*(S+1) for _ in range(N+1)]
dp[0][0]="_"
ab=[]
for i in range(N):
    a,b=map(int, input().split())
    ab.append((a,b))
    for k in range(S):
        if dp[i][k]!="":
            if k+a<=S:
                dp[i+1][k+a]="H"
            if k+b<=S:
                dp[i+1][k+b]="T"
if dp[N][S]=="":
    print("No")
else:
    print("Yes")
    rets=[""]*N
    now=S
    for i in range(N-1,-1,-1):
        rets[i]=dp[i+1][now]
        if rets[i]=="H":
            now-=ab[i][0]
        else:
            now-=ab[i][1]
    print("".join(rets))
