N,a,b=map(int, input().split())
array=list(map(int, input().split()))
ok=min(array)
ng=max(array)+1
while ok+1<ng:
    mid=(ok+ng)//2
    # mid以上にするために
    c=0
    for v in array:
        if v<mid:
            c+=(mid-v+a-1)//a
        else:
            c-=(v-mid)//b
    #print(mid,c)
    if c<=0:
        ok=mid
    else:
        ng=mid
print(ok)
