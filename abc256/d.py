N=int(input())
memo=[0]*(2*pow(10,5)+1)
for _ in range(N):
    l,r=map(int, input().split())
    memo[l]+=1
    memo[r]-=1
rets=[]
c=0
for i in range(2*pow(10,5)+1):
    if c==0 and memo[i]>0:
        rets.append([i])
    elif c>0 and c+memo[i]==0:
        rets[-1].append(i)
    c+=memo[i]
for ret in rets:
    print(*ret)
