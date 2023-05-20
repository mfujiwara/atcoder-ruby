import sys
N=int(input())
tkhs=[]
r=0
for _ in range(N):
    x,y,c=map(int, input().split())
    tkhs.append((x,y,c))
    r=max(r,max(abs(x),abs(y))*c)
l=-1
while True:
    if l+0.000001>r:
        print(r)
        sys.exit()
    mid=(l+r)/2
    min_x=-10**10
    max_x=10**10
    min_y=-10**10
    max_y=10**10
    for x,y,c in tkhs:
        diff=mid/c
        min_x=max(min_x,x-diff)
        max_x=min(max_x,x+diff)
        min_y=max(min_y,y-diff)
        max_y=min(max_y,y+diff)
    if min_x<=max_x and min_y<=max_y:
        r=mid
    else:
        l=mid
