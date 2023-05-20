H,W=map(int, input().split())
c=0
for _ in range(H):
    c+=input().count("#")
if c==H+W-1:
    print("Possible")
else:
    print("Impossible")
