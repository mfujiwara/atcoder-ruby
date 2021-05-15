from collections import defaultdict
N,X=map(int, input().split())
dp1=defaultdict(int)
dp2=defaultdict(int)
n1=N//2
n2=N-n1
for _ in range(n1):
    w=int(input())
    tmp={}
    tmp[w]=1
    for dw in dp1:
        total=dw+w
        if total<=X:
            tmp[total]=dp1[dw]
    for tw in tmp:
        dp1[tw]+=tmp[tw]
for _ in range(n2):
    w=int(input())
    tmp={}
    tmp[w]=1
    for dw in dp2:
        total=dw+w
        if total<=X:
            tmp[total]=dp2[dw]
    for tw in tmp:
        dp2[tw]+=tmp[tw]
dp1[0]=1
dp2[0]=1
ret=0
for key1 in dp1:
    v1=dp1[key1]
    v2=dp2[X-key1]
    ret+=v1*v2
print(ret)
