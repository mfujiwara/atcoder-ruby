INF=-(1<<60)
N,K=map(int, input().split())
array=list(map(int, input().split()))
sub_totals=[0]
for i,a in enumerate(array):
    if i<K:
        sub_totals[0]+=a
    else:
        sub_totals.append(sub_totals[-1]-array[i-K]+a)
dp=[INF]*N
dp1=[INF]*N
for i,a in enumerate(array):
    if i==0:
        dp[0]=max(0,a)
    elif i<=N-K:
        dp[i]=dp[i-1]+max(0,a)
    if i>=K:
        dp1[i]=max(dp1[i],dp1[i-1]+max(0,a))
    if i==0:
        dp1[i+K-1]=max(sub_totals[i],0)
    elif i<N-K+1:
        dp1[i+K-1]=dp[i-1]+max(sub_totals[i],0)
print(dp1[-1])
