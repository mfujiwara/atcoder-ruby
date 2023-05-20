MOD=pow(10,9)+7
N=int(input())
cAA=input()
cAB=input()
cBA=input()
cBB=input()
if N<=3:
    print(1)
elif cAB=="A":
    if cAA=="A":
        print(1)
    elif cBA=="B":
        print(pow(2,N-3,MOD))
    else:
        dp=[1,1]
        for _ in range(N-3):
            dp=[
                dp[1],
                (dp[0]+dp[1])%MOD
            ]
        print(dp[1])
else:
    if cBB=="B":
        print(1)
    elif cBA=="A":
        print(pow(2,N-3,MOD))
    else:
        dp=[1,1]
        for _ in range(N-3):
            dp=[
                dp[1],
                (dp[0]+dp[1])%MOD
            ]
        print(dp[1])
