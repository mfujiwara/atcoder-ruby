N=int(input())
array=list(map(int, input().split()))
ret=0
for i in range(1,N-1):
    if array[i-1]<array[i]<array[i+1] or array[i+1]<array[i]<array[i-1]:
        ret+=1
print(ret)
