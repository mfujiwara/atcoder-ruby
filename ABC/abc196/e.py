N=int(input())
all_val=None
max_x=10**9
min_x=-10**9
min_val=-10**9
for _ in range(N):
    a,t=map(int, input().split())
    if all_val==None:
        if t==1:
            min_val+=a
        elif t==2:
            max_val=min_val+(max_x-min_x)
            if min_val<a<max_val:
                diff=a-min_val
                min_x+=diff
                min_val+=diff
            elif max_val<=a:
                all_val=a
        else:
            max_val=min_val+(max_x-min_x)
            if min_val<a<max_val:
                diff=max_val-a
                max_x-=diff
            elif min_val>=a:
                all_val=a
    else:
        if t==1:
            all_val+=a
        elif t==2:
            all_val=max(all_val,a)
        else:
            all_val=min(all_val,a)
Q=int(input())
array=list(map(int, input().split()))
max_val=min_val+(max_x-min_x)
for x in array:
    if all_val!=None:
        print(all_val)
    elif x<=min_x:
        print(min_val)
    elif min_x<x<max_x:
        print(min_val+x-min_x)
    else:
        print(max_val)
