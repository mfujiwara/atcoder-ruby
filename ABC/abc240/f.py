T=int(input())
for _ in range(T):
    N,M=map(int, input().split())
    ret=-5
    b_now=0
    a_now=0
    xy=[]
    for i in range(N):
        x,y=map(int, input().split())
        if i==0:
            ret=x
        xy.append((x,y))
    for x,y in xy:
        # 初項 b_now+x, 項差 x, 項数 y
        if b_now+x>0 and b_now+x*y<0:
            y1=-b_now//x
            y2=y-y1
            s1=y1*(2*(b_now+x)+(y1-1)*x)//2
            s2=y2*(2*(b_now+x*y1+x)+(y2-1)*x)//2
        else:
            s1=y*(2*(b_now+x)+(y-1)*x)//2
            s2=0
        a_now+=s1
        ret=max(ret,a_now)
        a_now+=s2
        ret=max(ret,a_now)
        b_now+=x*y
    print(ret)
