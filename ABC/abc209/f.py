MOD=pow(10,9)+7
N=int(input())
array=list(map(int, input().split()))
# dp[i]:=ある本数以下の木だけで考えた時, 最後の木がi番目に伐採される場合の数
dp = [[0]*N for i in range(N)]
dp[0]= 1
for i in range(1,N):
    # i本の木だけ考えた時、i本目が何番目に伐採される場合の数を求めていく
    nexts=[0]*N
    if array[i-1]<array[i]:
        # i-1番目の木よりも先に切る
        for j in range(1,i+1):
            nexts[j]=(nexts[j-1]+dp[j-1])%MOD
    elif array[i-1]>array[i]:
        # i-1番目の木よりも後に切る
        for j in range(i-1,-1,-1):
            nexts[j]=(nexts[j+1]+dp[j])%MOD
    else:
        # 自由
        total=0
        for j in range(i):
            total+=dp[j]
            total%=MOD
        for j in range(i+1):
            nexts[j]=total
    dp=nexts
	#print(dp[i])
ret=0
for i in range(N):
    ret+=dp[i]
    ret%=MOD
print(ret)
