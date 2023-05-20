MOD=998244353
A,B,C,D=map(int, input().split())
rets=[[0]*(D-B+1) for _ in range(C-A+1)]
rets[0][0]=1
for i in range(C-A+1):
    for j in range(D-B+1):
        if i==0:
            if j==0:
                continue
            else:
                rets[i][j]=rets[i][j-1]*A
                rets[i][j]%=MOD
        else:
            if j==0:
                rets[i][j]=rets[i-1][j]*B
                rets[i][j]%=MOD
            else:
                rets[i][j]=rets[i-1][j]*(B+j)
                rets[i][j]%=MOD
                rets[i][j]+=rets[i][j-1]*(A+i)
                rets[i][j]%=MOD
                rets[i][j]-=rets[i-1][j-1]*(A+i-1)*(B+j-1)
                rets[i][j]%=MOD
print(rets[-1][-1])
