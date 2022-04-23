N=int(input())
array=list(map(int, input().split()))
L=int(input())
array.append(array[-1]+L)
dp=[[] for _ in range(N)] # dp[i][j]:=i番目のホテルから2^j日以内に行けるホテルの番号
# dp[i][0]を埋める
target=0
for i in range(2,N+1):
    while array[i]-array[target]>L:
        dp[target].append(i-1)
        target+=1
dp[-1].append(N)
# 最後まで埋める
while dp[0][-1]!=N:
    for i in range(len(dp)-1):
        if dp[i][-1]==N:
            break
        dp[i].append(dp[dp[i][-1]][-1])
Q=int(input())
for _ in range(Q):
    a,b=map(int, input().split())
    a-=1
    b-=1
    if a>b:
        a,b=b,a
    def calc(start,end):
        if dp[start][0]>=end:
            return 0
        ok=0
        ng=len(dp[start])-1
        while ok+1<ng:
            mid=(ok+ng)//2
            if dp[start][mid]<=end:
                ok=mid
            else:
                ng=mid
        return ok
    ret=0
    while a<b:
        k=calc(a,b)
        ret+=pow(2,k)
        a=dp[a][k]
    print(ret)
