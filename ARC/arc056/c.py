N,K=map(int, input().split())
W=[list(map(int, input().split())) for _ in range(N)]
total=0
for i in range(N-1):
    for j in range(i+1,N):
        total+=W[i][j]
# dp[bit]:=bitが立っている集合に対する答えにtotalを足した値
dp=[0]*pow(2,N) 
for bit in range(1,pow(2,N)):
    array=[]
    bb=bit
    k=0
    while bb>0:
        bb,r=divmod(bb,2)
        if r==1:
            array.append(k)
        k+=1
    v=K
    for i in range(len(array)):
        for j in range(i+1,len(array)):
                v+=W[array[i]][array[j]]
    n_bit=(bit-1)&bit
    while n_bit>0:
        v=max(v,dp[n_bit]+dp[bit^n_bit])
        n_bit=(n_bit-1)&bit
    dp[bit]=v
print(dp[-1]-total)
