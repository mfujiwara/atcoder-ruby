N,M=map(int, input().split())
right=M+1
left=0
while left+1!=right:
    mid=(left+right)//2
    if M>=2*mid and N+(M-2*mid)//2>=mid:
        left=mid
    else:
        right=mid
print(left)
