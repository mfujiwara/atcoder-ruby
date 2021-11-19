array=list(map(int, input().split()))
rets=[]
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            rets.append(array[i]+array[j]+array[k])
rets.sort(reverse=True)
print(rets[2])
