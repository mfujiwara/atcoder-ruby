N,L,W=map(int, input().split())
array=list(map(int, input().split()))
now=0
ret=0
for a in array:
    if now<a:
        ret+=(a-now+W-1)//W
        now=a+W
    else:
        now=max(now,a+W)
if now<L:
    ret+=(L-now+W-1)//W
print(ret)
