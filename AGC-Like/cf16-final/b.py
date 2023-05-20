N=int(input())
left=0
right=N
while True:
    if left+1==right:
        n=right
        while N>0:
            print(n)
            N-=n
            n=min(n-1,N)
        exit()
    mid=(left+right)//2
    if (mid+1)*mid//2 >= N:
        right=mid
    else:
        left=mid
