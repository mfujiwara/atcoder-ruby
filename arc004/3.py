import math
X,Y=map(int, input().split("/"))
g=math.gcd(X,Y)
X//=g
Y//=g
found=False
s=int((2*X-Y)/Y)
for i in range(3):
    n=s+i
    mY=(n*(n+1)//2*Y)-X*n
    if mY%Y!=0:
        continue
    m=mY//Y
    if 0<m<=n:
        print(n,m) 
        found=True
if not found:
    print("Impossible")
