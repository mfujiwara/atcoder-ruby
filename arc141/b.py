MOD=998244353
N,M=map(int, input().split())
array=[1]
sums=[1]
while sums[-1]<M:
    sums.append(((sums[-1]+1)*2-1))
    array.append((sums[-1]-sums[-2]))
diff=sums[-1]-M
sums[-1]-=diff
array[-1]-=diff
#print(array)
if len(array)<N:
    print(0)
    exit()
dp=array
for _ in range(N-1):
    nexts=[0]*len(array)
    total=0
    for i in range(len(array)-1):
        total+=dp[i]
        total%=MOD
        nexts[i+1]=total*array[i+1]%MOD
    dp=nexts
    #print(dp)
ret=0
for d in dp:
    ret+=d
    ret%=MOD
print(ret)
