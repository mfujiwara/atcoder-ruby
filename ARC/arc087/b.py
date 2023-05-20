s=input()
X,Y=map(int, input().split())
xs=[0]
x_sum=0
ys=[]
y_sum=0
direction_x=True
for ch in s:
    if ch=="F":
        if direction_x:
            xs[-1]+=1
            x_sum+=1
        else:
            ys[-1]+=1
            y_sum+=1
    else:
        if direction_x:
            ys.append(0)
            direction_x=False
        else:
            xs.append(0)
            direction_x=True
x_sum-=xs[0]
X-=xs[0]
xs=xs[1:]
X=abs(X)
Y=abs(Y)
if x_sum<X or y_sum<Y or (x_sum-X)%2==1 or abs(y_sum-Y)%2==1:
    print("No")
    exit()
dp_x=[False]*(abs(X-x_sum)//2+1)
dp_x[0]=True
dp_y=[False]*(abs(Y-y_sum)//2+1)
dp_y[0]=True
for dx in xs:
    for i in range(len(dp_x))[::-1]:
        if i+dx<len(dp_x) and dp_x[i]:
            dp_x[i+dx]=True
for dy in ys:
    for i in range(len(dp_y))[::-1]:
        if i+dy<len(dp_y) and dp_y[i]:
            dp_y[i+dy]=True
if dp_x[-1] and dp_y[-1]:
    print("Yes")
else:
    print("No")
