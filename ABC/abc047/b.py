W,H,N=map(int, input().split())
a1=0
a2=W
a3=0
a4=H
for _ in range(N):
    x,y,a=map(int, input().split())
    if a==1:
        a1=max(a1,x)
    elif a==2:
        a2=min(a2,x)
    elif a==3:
        a3=max(a3,y)
    else:
        a4=min(a4,y)
print(max(0,a2-a1)*max(0,a4-a3))
