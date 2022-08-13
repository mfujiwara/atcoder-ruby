R,C=map(int, input().split())
d=max(abs(R-8),abs(C-8))
if d%2==0:
    print("white")
else:
    print("black")
