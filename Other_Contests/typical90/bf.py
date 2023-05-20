MOD=10**5
N,K=map(int, input().split())
if N==0:
    print(0)
    exit()
memo={}
memo[N]=0
i=0
while i<K:
    x=N
    y=0
    while x>0:
        x,r=divmod(x,10)
        y+=r
    N=(N+y)%MOD
    if N not in memo:
        memo[N]=i
    else:
        mod=(i-memo[N])
        d=(K-i-1)//mod
        i+=d*mod
    i+=1
print(N)
