N,T=map(int, input().split())
array=list(map(int, input().split()))
ret=0
for i in range(N):
    if i<N-1:
        ret+=min(T,array[i+1]-array[i])
    else:
        ret+=T
print(ret)
