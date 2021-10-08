MOD=998244353
N=int(input())
array=list(map(int, input().split()))
memo=[0]*10
memo[array[0]]+=1
for i in range(1,N):
    nexts=[0]*10
    a=array[i]
    for b in range(10):
        c=(a+b)%10
        d=(a*b)%10
        nexts[c]+=memo[b]
        nexts[c]%=MOD
        nexts[d]+=memo[b]
        nexts[d]%=MOD
    memo=nexts
for m in memo:
    print(m)
