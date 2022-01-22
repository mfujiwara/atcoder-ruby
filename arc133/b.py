import bisect
N=int(input())
p_array=list(map(int, input().split()))
q_array=list(map(int, input().split()))
p_indexes=[[] for _ in range(N+1)] # p_indexes[q]:= qとペアになりうるp_arrayのindex
for i,p in enumerate(p_array):
    pp=p
    while pp<=N:
        p_indexes[pp].append(i)
        pp+=p
dp=[N+1]*N # dp[i]:= i+1の長さを実現する最小のpのindex
ret=0
for i,q in enumerate(q_array):
    for p_ind in p_indexes[q][::-1]:
        ind=bisect.bisect_left(dp,p_ind)
        dp[ind]=p_ind
        ret=max(ret,ind+1)
print(ret)
