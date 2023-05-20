N=int(input())
array=list(map(int, input().split()))
acc=[0]
for i in range(N-1):
    acc.append(acc[-1]^array[i])
for i in range(N-2,-1,-1):
    acc[i]=array[i]^array[i+1]^acc[i+1]
print(*acc)
