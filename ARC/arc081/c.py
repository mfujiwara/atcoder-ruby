A=input().rstrip()
L=len(A)
dp=[(0, L)]*26 # dp[d]:=最初に文字dが現れた後にある26種類の文字セットの数-1とindex
ord_a=ord("a")
nexts=[None]*L # nexts[i]:=indexの文字dに繋げると答え
for i,c in list(enumerate(A))[::-1]:
    res=(10**18,0,0) # 後ろにある文字セットの数, 文字, index
    for d in range(26):
        res=min(res,(dp[d][0],d,dp[d][1]))
    x,d,j=res
    nexts[i]=(j,d)
    dp[ord(c)-ord_a]=(x+1,i)
# 後ろにある文字セット数が少ない文字の最小を探す
res=(10**18,0,0)
for d in range(26):
    res=min(res,(dp[d][0],d,dp[d][1]))
x,d,index=res
# nextsをもとに答えを成形
rets=[chr(d+ord_a)]
while index<L:
    index,d=nexts[index]
    rets.append(chr(d+ord_a))
print("".join(rets))
