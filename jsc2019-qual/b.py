MOD=pow(10,9)+7
N,K=map(int, input().split())
array=list(map(int, input().split()))
counts=[[0,0] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if array[i]>array[j]:
            counts[i][0]+=1
            if i<j:
                counts[i][1]+=1
ret=0
for a,b in counts:
    ret+=(b+b+a*(K-1))*K//2
    ret%=MOD
print(ret)
