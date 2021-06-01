N=int(input())
xy=[]
yx=[]
for i in range(N):
    x,y=map(int, input().split())
    xy.append((x,y,i))
    yx.append((y,x,i))
xy=sorted(xy)
yx=sorted(yx)
max_diff_x=xy[-1][0]-xy[0][0]
max_diff_y=yx[-1][0]-yx[0][0]
if max_diff_x==max_diff_y:
    if (xy[0][2]==yx[0][2] and xy[-1][2]==yx[-1][2]) or (xy[0][2]==yx[-1][2] and xy[-1][2]==yx[0][2]):
        ret=0
        ret=max(ret,xy[-1][0]-xy[1][0],xy[-2][0]-xy[0][0])
        ret=max(ret,yx[-1][0]-yx[1][0],yx[-2][0]-yx[0][0])
        print(ret)
    else:
        print(max_diff_x)
elif max_diff_x>max_diff_y:
    ret=max_diff_y
    ret=max(ret,xy[-1][0]-xy[1][0],xy[-2][0]-xy[0][0])
    print(ret)
else:
    ret=max_diff_x
    ret=max(ret,yx[-1][0]-yx[1][0],yx[-2][0]-yx[0][0])
    print(ret)
