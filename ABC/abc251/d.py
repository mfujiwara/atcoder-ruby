W=int(input())
array=[]
for i in [1,100,10000]:
    for j in range(1,100):
        array.append(i*j)
print(len(array))
print(*array)
