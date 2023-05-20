N=int(input())
array=list(map(int, input().split()))
ret=1
d=0
pre=array[0]
for i in range(1,N):
    if d==0:
        if pre>array[i]:
            d=-1
        elif pre<array[i]:
            d=1
    elif d==1:
        if pre>array[i]:
            ret+=1
            d=0
    else:
        if pre<array[i]:
            ret+=1
            d=0
    pre=array[i]
print(ret)
