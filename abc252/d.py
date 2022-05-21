import collections
N=int(input())
array=list(map(int, input().split()))
dp=[0]*4
dp[0]=1
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
for a,c in counts.items():
    for i in range(3):
        dp[3-i]+=dp[2-i]*c
print(dp[-1])
