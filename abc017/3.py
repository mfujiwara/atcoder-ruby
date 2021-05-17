N,M=map(int, input().split())
memo=[0]*(M+2)
for _ in range(N):
    l,r,s=map(int, input().split())
    memo[0]+=s
    memo[l]-=s
    memo[r+1]+=s
sums=[0]
for v in memo:
    sums.append(sums[-1]+v)
sums=sums[2:-1]
print(max(sums))
