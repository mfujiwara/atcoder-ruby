def is_ku(a,b,c):
    for (ax,ay),(bx,by),(cx,cy) in [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)]:
        if ax==bx and ay==cy and abs(ay-by)==1 and abs(ax-cx)==1:
            return True
    return False
T=int(input())
for _ in range(T):
    ax,ay,bx,by,cx,cy=map(int, input().split())
    a,b,c=sorted([(ax,ay),(bx,by),(cx,cy)])
    if b[0]!=c[0] and b[1]!=c[1]:
        # 左下
        if a[0]==0 and a[1]==0:
            print(0)
        elif a[0]==a[1]:
            print(abs(a[0])*2+1)
        else:
            print(max(abs(a[0]),abs(a[1]))*2)
    elif a[0]!=b[0] and a[1]!=b[1]:
        # 右上
        if c[0]==c[1]:
            if c[0]>=2:
                print(c[0]*2)
            elif c[0]<=0:
                print(-c[0]*2+2)
            else:
                print(1)
        else:
            print(max(abs(2*c[0]-1),abs(2*c[1]-1)))
    elif a[0]==b[0]:
        # 左上
        if b[1]<=0:
            if abs(b[0])<=abs(b[1]):
                print(-b[1]*2+1)
            else:
                print(abs(b[0])*2)
        else:
            if abs(b[0])<=abs(b[1])-1:
                print(b[1]*2-1)
            else:
                print(abs(b[0])*2)
    else:
        # 右下
        if b[0]<=0:
            if abs(b[1])<=abs(b[0]):
                print(-b[0]*2+1)
            else:
                print(abs(b[1])*2)
        else:
            if abs(b[1])<=abs(b[0])-1:
                print(b[0]*2-1)
            else:
                print(abs(b[1])*2)
