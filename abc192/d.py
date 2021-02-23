import sys
X=input()
M=int(input())
xx=int(max(list(X)))

if len(X)==1:
    if int(X)<=M:
        print(1)
    else:
        print(0)
    sys.exit()

r=0
for x in X:
    r*=(xx+1)
    r+=int(x)
if r>M:
    print(0)
    sys.exit()
r=0    

left=xx+1
right=M+1
while True:
    if left+1==right:
        print(left-xx)
        sys.exit()
    mid=(left+right)//2
    r=0
    for x in X:
        r*=mid
        r+=int(x)
    if r<=M:
        left=mid
    else:
        right=mid
