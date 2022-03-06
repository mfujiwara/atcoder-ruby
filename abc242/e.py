MOD=998244353
T=int(input())
ordA=ord("A")
rets=[]
for _ in range(T):
    N=int(input())
    S=input()
    if N%2==0:
        dp=[0,1] # dp[0]:=超えない, dp[1]:=同じ
        for i in range(len(S)//2):
            ch=S[i]
            nexts=[0]*2
            v=ord(ch)-ordA
            nexts[0]=(dp[0]*26%MOD+dp[1]*v%MOD)%MOD
            nexts[1]=dp[1]
            dp=nexts
        s=S[:len(S)//2]
        t=s+s[::-1]
        if t>S:
            dp[1]-=1
        print(sum(dp)%MOD)
        #rets.append(sum(dp)%MOD)
    else:
        dp=[0,1] # dp[0]:=超えない, dp[1]:=同じ
        for i in range((len(S)+1)//2):
            ch=S[i]
            nexts=[0]*2
            v=ord(ch)-ordA
            nexts[0]=(dp[0]*26%MOD+dp[1]*v%MOD)%MOD
            nexts[1]=dp[1]
            dp=nexts
        s=S[:len(S)//2+1]
        t=s+s[:-1][::-1]
        if t>S:
            dp[1]-=1
        print(sum(dp)%MOD)
        #rets.append(sum(dp)%MOD)
#print(rets)
