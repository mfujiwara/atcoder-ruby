N=int(input())
array=list(map(int, input().split()))
array.sort()
array=list(map(str,array[-3:]))
rets=[
    int(array[0]+array[1]+array[2]),
    int(array[0]+array[2]+array[1]),
    int(array[1]+array[0]+array[2]),
    int(array[1]+array[2]+array[0]),
    int(array[2]+array[0]+array[1]),
    int(array[2]+array[1]+array[0])
]
print(max(rets))
