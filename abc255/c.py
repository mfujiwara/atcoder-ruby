X,A,D,N=map(int, input().split())
if D<0:
    A=A+D*(N-1)
    D=-D
if X<=A:
    print(A-X)
    exit()
last=A+D*(N-1)
if X>=last:
    print(X-last)
    exit()
left=1 # より大きい
right=N # 以下
while left+1!=right:
    mid=(left+right)//2
    m=A+D*(mid-1)
    if X>m:
        left=mid
    else:
        right=mid
ll=A+D*(left-1)
rr=A+D*(right-1)
print(min(X-ll,rr-X))
