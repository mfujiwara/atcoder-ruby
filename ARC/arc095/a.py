N=int(input())
array=list(map(int, input().split()))
sorted_array=sorted(array)
m1=sorted_array[(N+1)//2-1]
m2=sorted_array[(N+1)//2]
for a in array:
    if a <=m1:
        print(m2)
    elif a>=m2:
        print(m1)
