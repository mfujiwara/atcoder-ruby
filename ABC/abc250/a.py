H,W=map(int, input().split())
R,C=map(int, input().split())
if H==1 and W==1:
    print(0)
    exit()
if H==1 or W==1:
    if (R,C) in [(1,1),(H,1),(1,W),(H,W)]:
        print(1)
    else:
        print(2)
    exit()
if (R,C) in [(1,1),(H,1),(1,W),(H,W)]:
    print(2)
elif R==1 or R==H or C==1 or C==W:
    print(3)
else:
    print(4)
