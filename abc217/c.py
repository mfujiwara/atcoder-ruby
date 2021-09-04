N=int(input())
array=list(map(int, input().split()))
Q=[-1]*N
for i in range(N):
    p=array[i]
    Q[p-1]=i+1
print(*Q)
