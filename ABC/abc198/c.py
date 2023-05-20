R,X,Y=map(int, input().split())
xy=X*X+Y*Y
left=0
right=10**6
while True:
    if left+1==right:
        break
    mid=(left+right)//2
    if mid*mid*R*R>=xy:
        right=mid
    else:
        left=mid
if right==1 and R*R>xy:
    print(2)
else:
    print(right)
