import bisect
N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
ret=pow(10,6)
reach=pow(10,10)
must=0
for i in range(N-1,-1,-1):
    a=a_array[i]
    b=b_array[i]
    if a<=b:
        r=max(b-a+1,must)
        ret=min(ret,r)
        if a<reach:
            must+=1
    else:
        reach=min(reach,a-b)
print(min(ret,must))
