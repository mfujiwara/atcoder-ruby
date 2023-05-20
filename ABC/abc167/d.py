N,K=map(int, input().split())
array=list(map(int, input().split()))
memo=[-1]*N
memo[0]=K
now=0
while K>0:
    now=array[now]-1
    K-=1
    if memo[now]>0:
        break
    memo[now]=K
if K==0:
    print(now+1)
else:
    d=memo[now]-K
    K%=d
    while K>0:
        now=array[now]-1
        K-=1
    print(now+1)
