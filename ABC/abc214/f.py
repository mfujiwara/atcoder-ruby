MOD=pow(10,9)+7
S=input()
left=[(-1,-1)]*26
dp=[0]*(len(S)+1)
dp[0]=1
ord_a=ord("a")
for i,ch in enumerate(S):
    ch=ord(ch)-ord_a
    dp[i+1]=1
    for j in range(26):
        if left[j][0]!=-1 and left[j][0]!=i-1:
            dp[i+1]+=dp[left[j][0]+1]
            dp[i+1]%=MOD
        elif left[j][1]!=-1:
            dp[i+1]+=dp[left[j][1]+1]
            dp[i+1]%=MOD
    left[ch]=(i,left[ch][0])
ret=0
for ch in range(26):
    if left[ch][0]!=-1:
        ret+=dp[left[ch][0]+1]
        ret%=MOD
print(ret)
