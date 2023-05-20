N,W=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
memo=set()
for i in range(N):
    if array[i]>W: break
    memo.add(array[i])
    for j in range(i):
        if array[i]+array[j]>W: break
        memo.add(array[i]+array[j])
        for k in range(j):
            if array[i]+array[j]+array[k]>W: break
            memo.add(array[i]+array[j]+array[k])
print(len(memo))
