C=int(input())
rets=[0]*3
for _ in range(C):
    array=list(map(int, input().split()))
    array.sort()
    for i in range(3):
        rets[i]=max(rets[i],array[i])
print(rets[0]*rets[1]*rets[2])
