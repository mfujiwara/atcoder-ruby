N,K=map(int, input().split())
MATRIX=[list(map(int, input().split())) for _ in range(N)]
decide_set=set()
decide_nums=[0]*N
L=K
for i in range(N):
    rets=set()
    l_updated=True
    while l_updated:
        l_updated=False
        for j in range(i+1):
            q,r=divmod(L,N)
            t=q+(1 if j<r else 0)
            if decide_nums[j]!=t:
                for k in range(decide_nums[j],t):
                    decide_nums[j]+=1
                    if MATRIX[j][k] not in decide_set:
                        rets.add(MATRIX[j][k])
                        decide_set.add(MATRIX[j][k])
                    else:
                        L+=1
                        l_updated=True
    print(*sorted(rets))
