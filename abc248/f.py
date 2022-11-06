N,P=map(int, input().split())
dp0=[0]*N # 上下が連結している
dp1=[0]*N # 上下が連結していない
dp0[0]=1
dp1[1]=1
for _ in range(N-1):
    nexts0=[0]*N
    nexts1=[0]*N
    for i in range(N):
        nexts0[i]+=dp0[i]+dp1[i]
        nexts0[i]%=P
        if i+1>=N: continue
        nexts0[i+1]+=dp0[i]*3
        nexts0[i+1]%=P
        nexts1[i+1]+=dp1[i]
        nexts1[i+1]%=P
        if i+2>=N: continue
        nexts1[i+2]+=dp0[i]*2
        nexts1[i+2]%=P
    dp0=nexts0
    dp1=nexts1
print(*dp0[1:])
