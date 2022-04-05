import collections


N,X=map(int, input().split())
array=list(map(int, input().split()))
# dp[i][j]:=大きい方からiまで決めて、支払い残りがjの場合の数
dp=collections.defaultdict(int)
dp[X]=1
for i in range(N-1,-1,-1):
    a=array[i]
    nexts=collections.defaultdict(int)
    for d in dp:
        q,r=divmod(d,a)
        if i==N-1 or abs(q)<array[i+1]//array[i]:
            nexts[r]+=dp[d]
        if r!=0 and (i==N-1 or abs(q+1)<array[i+1]//array[i]):
            nexts[r-a]+=dp[d]
    dp=nexts
print(dp[0])
