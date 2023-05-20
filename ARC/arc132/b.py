n=int(input())
array=list(map(int, input().split()))
if (array[0]+1)%n==array[1]%n:
    if array[0]==1:
        print(0)
    else:
        v1=n-array[0]+1
        v2=array[0]+1
        print(min(v1,v2))
else:
    if array[0]==n:
        print(1)
    else:
        v1=array[0]+1
        v2=1+n-array[0]
        print(min(v1,v2))
