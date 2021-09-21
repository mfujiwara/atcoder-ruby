R,B=map(int, input().split())
x,y=map(int, input().split())
left=0
right=R+B
while True:
    if left+1==right:
        print(left)
        exit()
    mid=(left+right)//2
    if R>=mid and B>=mid and (R-mid)//(x-1)+(B-mid)//(y-1)>=mid:
        left=mid
    else:
        right=mid
