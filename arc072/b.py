X,Y=map(int, input().split())
#L 0,1 1,1
#W 0,2 0,3
#L 1,2 2,2
#W 0,4 0,5 0,6 1,3 1,4
#L 2,3 3,3
#W 0,7 0,8 0,9 1,5 1,6 1,7 2,4 2,5
#L 3,4 4,4
if abs(X-Y)<=1:
    print("Brown")
else:
    print("Alice")
