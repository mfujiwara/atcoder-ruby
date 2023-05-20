H,W=map(int, input().split())
A=[input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if j==0:
            print("#",end="")
        elif j==W-1:
            print(".",end="")
        else:
            if A[i][j]=="#":
                print("#",end="")
            elif i%2==0:
                print("#",end="")
            else:
                print(".",end="")
    print()
print()
for i in range(H):
    for j in range(W):
        if j==0:
            print(".",end="")
        elif j==W-1:
            print("#",end="")
        else:
            if A[i][j]=="#":
                print("#",end="")
            elif i%2==1:
                print("#",end="")
            else:
                print(".",end="")
    print()
