import math
import bisect
N,M=map(int, input().split())
array=list(map(int, input().split()))
needs=[-1,2,5,5,4,5,6,3,7,6]
useable=dict()
for a in array:
    need=needs[a]
    if (need in useable):
        useable[need]=max(useable[need],a)
    else:
        useable[need]=a
dp=[[-1] for _ in range(N+1)]
dp[0]=[]
def large(a,b):
    if len(a)>len(b):
        return a
    elif len(a)<len(b):
        return b
    else:
        for i in range(len(a)-1,-1,-1):
            if a[i]>b[i]:
                return a
            elif a[i]<b[i]:
                return b
    return a
for i in range(N+1):
    if dp[i]==[-1]: continue
    for j in useable:
        if i+j<N+1:
            tmp=dp[i][:]
            bisect.insort_left(tmp,useable[j])
            dp[i+j]=large(dp[i+j],tmp)
base=dp[-1]
for i in range(len(base)):
    print(base[-1-i], end="")
print("")
