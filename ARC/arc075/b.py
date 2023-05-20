import sys
N,A,B=map(int, input().split())
max_h=0
hs=[]
for _ in range(N):
    h=int(input())
    max_h=max(max_h,h)
    hs.append(h)
left=0
right=10**14#(max_h+A-1)//A*N
while True:
    if left+1==right:
        print(right)
        sys.exit()
    mid=(left+right)//2
    c=0
    for h in hs:
        h-=B*mid
        if h>0:
            c+=(h+A-B-1)//(A-B)
    if c<=mid:
        right=mid
    else:
        left=mid
