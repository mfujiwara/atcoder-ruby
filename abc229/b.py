A,B=map(int, input().split())
while A!=0 and B!=0:
    if A%10+B%10>9:
        print("Hard")
        exit()
    else:
        A//=10
        B//=10
print("Easy")
