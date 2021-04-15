N,K=map(int, input().split())
ret=0
for ab in range(2,2*N+1):
    cd=ab-K
    if cd<2 or 2*N<cd: continue
    x=ab-1 if ab<=N+1 else 2*N+1-ab
    y=cd-1 if cd<=N+1 else 2*N+1-cd
    ret+=x*y
print(ret)
