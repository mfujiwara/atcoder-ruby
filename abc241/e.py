N,K=map(int, input().split())
array=list(map(int, input().split()))
memo={}
total=0
while K>0:
    if total%N in memo:
        v,k=memo[total%N]
        diff_k=k-K
        diff_x=total-v
        q,r=divmod(K-1,diff_k)
        K=r
        total+=diff_x*q
        total+=array[total%N]
    else:
        memo[total%N]=(total,K)
        total+=array[total%N]
        K-=1
print(total)
