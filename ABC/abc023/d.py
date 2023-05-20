N=int(input())
left=0
right=0
hs=[]
for _ in range(N):
    h,s=map(int, input().split())
    hs.append((h,s))
    right=max(right,h+s*(N-1))
while True:
    if left+1==right:
        print(right)
        exit()
    mid=(left+right)//2
    queue=[]
    for h,s in hs:
        # h+x*s<=mid
        x=(mid-h)//s
        queue.append(x)
    queue.sort()
    valid=True
    for i in range(N):
        if i>queue[i]:
            valid=False
            break
    if valid:
        right=mid
    else:
        left=mid
