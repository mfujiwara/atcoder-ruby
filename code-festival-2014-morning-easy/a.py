N=int(input())
array=list(map(int, input().split()))
ret=0
for i in range(N-1):
    ret+=array[i+1]-array[i]
print(ret/(N-1))
