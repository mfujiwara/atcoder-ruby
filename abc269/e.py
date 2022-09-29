N=int(input())
ok=0
ng=N
while ok+1!=ng:
    mid=(ok+ng)//2
    print("?",1,N,1,mid,flush=True)
    t=int(input())
    if t==mid:
        ok=mid
    else:
        ng=mid
y=ng
ok=0
ng=N
while ok+1!=ng:
    mid=(ok+ng)//2
    print("?",1,mid,1,N,flush=True)
    t=int(input())
    if t==mid:
        ok=mid
    else:
        ng=mid
x=ng
print("!",x,y,flush=True)
