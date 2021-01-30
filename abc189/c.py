N=int(input())
array=list(map(int, input().split()))
ret=0
for i in range(N):
    min_x=array[i]
    for j in range(i,N):
        min_x=min(min_x,array[j])
        ret=max(ret,(j-i+1)*min_x)
print(ret)
