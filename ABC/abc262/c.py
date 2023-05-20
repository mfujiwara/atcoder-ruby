N=int(input())
array=list(map(int, input().split()))
c=0
d=0
for i,a in enumerate(array):
    if i+1==a:
        c+=1
    elif array[a-1]==i+1:
        d+=1
ret=c*(c-1)//2+d//2
print(ret)
