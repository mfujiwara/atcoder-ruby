N,M=map(int, input().split())
xs=[]
for _ in range(M):
    x=int(input())
    xs.append(x)
left=-1
right=2*N
while True:
    if left+1==right:
        print(right)
        exit()
    mid=(left+right)//2
    k=0
    for x in xs:
        if k+1<x-mid:
            break
        if k+1>=x:
            k=x+mid
        else:
            k1=x+(mid-(x-k-1))//2
            k2=k+mid-(x-k-1)+1
            k=max(k1,k2)
    if k>=N:
        right=mid
    else:
        left=mid
