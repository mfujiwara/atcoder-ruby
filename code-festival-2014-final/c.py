def Base_n_to_10(X,n):
    out = 0
    X=str(X)
    for i in range(1,len(X)+1):
        out += int(X[-i])*(n**(i-1))
    return out
A=int(input())
if A==10:
    print(10)
    exit()
if A==10**16:
    print(10000)
    exit()
if A<10:
    print(-1)
    exit()
left=10
right=10000
while True:
    if left+1==right:
        print(-1)
        exit()
    mid=(left+right)//2
    v=Base_n_to_10(mid,mid)
    if v==A:
        print(mid)
        exit()
    if v>A:
        right=mid
    else:
        left=mid
