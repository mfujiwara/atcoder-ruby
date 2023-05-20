N,K=map(int, input().split())
array=list(map(int, input().split()))
if sum(array)<K:
    print(N)
    exit()
uniqs=[0]+sorted(list(set(array)))
def calc(mid):
    if mid>=K:
        return True
    dp=[False]*K
    dp[0]=True
    passed=False
    for a in array:
        if a==mid and not passed:
            passed=True
            continue
        for t in range(K-1,-1,-1):
            if dp[t] and t+a<K:
                dp[t+a]=True
                if K-mid<=t+a:
                    return True
    return False
# left以下は全部不要, right以下は必要なものもある
left=0
right=len(uniqs)
while left+1!=right:
    mid=(left+right)//2
    if calc(uniqs[mid]):
        right=mid
    else:
        left=mid
print(len([a for a in array if a<=uniqs[left]]))
