X,Y,Z=map(int, input().split())
#W/Z<Y/X
W=Y*Z//X
if W*X==Y*Z:
    W-=1
print(W)
