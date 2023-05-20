N,K=map(int, input().split())
array=list(map(int, input().split()))
array.sort(reverse=True)
ret=0
for i in range(K):
    ret+=array[i]/pow(2,i+1)
print(ret)
