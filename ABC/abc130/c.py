W,H,x,y=map(int, input().split())
if x*2==W and y*2==H:
    t=1
else:
    t=0
print(W*H/2,t)
