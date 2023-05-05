X,Y=map(int, input().split())
for x1 in range(X+1):
    x2=X-x1
    if x1*4+x2*2==Y:
        print("Yes")
        exit()
print("No")
