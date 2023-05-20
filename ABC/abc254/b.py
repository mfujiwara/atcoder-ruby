N=int(input())
array=[1]
print(*array)
for _ in range(N-1):
    array.append(array[-1])
    for i in range(len(array)-2,0,-1):
        array[i]=array[i]+array[i-1]
    print(*array)
