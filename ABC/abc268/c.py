N=int(input())
array=list(map(int, input().split()))
count=[0]*N
for i,a in enumerate(array):
    count[(i-a-1)%N]+=1
    count[(i-a)%N]+=1
    count[(i-a+1)%N]+=1
print(max(count))
