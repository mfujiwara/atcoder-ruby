N=int(input())
array=list(map(int, input().split()))
max0=0
now0=0
max1=0
now1=0
for a in array:
    if a==0:
        now0+=1
        now1=max(0,now1-1)
        max0=max(max0,now0)
    else:
        now1+=1
        now0=max(0,now0-1)
        max1=max(max1,now1)
print(max1+max0+1)
