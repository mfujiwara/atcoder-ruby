MOD=998244353
N,D=map(int, input().split())
array=list(map(int, input().split()))
BIT=pow(2,2*D+1)
dp=[0]*BIT
dp[pow(2,D+1)-1]=1
for index,a in enumerate(array):
    nexts=[0]*BIT
    if a==-1:
        for i in range(BIT):
            if i&1==0:continue
            k=i>>1
            for j in range(2*D+1):
                if k>>j&1==0:
                    bit=k|1<<j
                    nexts[bit]+=dp[i]
                    nexts[bit]%=MOD
    else:
        b=pow(2,a-1-index+D)
        if b<1:
            print(0)
            exit()
        for i in range(BIT):
            if i&1==0:continue
            k=i>>1
            if k&b==0:
                bit=k|b
                nexts[bit]+=dp[i]
                nexts[bit]%=MOD
    dp=nexts
print(dp[pow(2,D+1)-1])
