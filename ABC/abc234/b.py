N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
ret=0
for i in range(N-1):
    x1,y1=xy[i]
    for j in range(i+1,N):
        x2,y2=xy[j]
        ret=max(ret,pow(x1-x2,2)+pow(y1-y2,2))
print(pow(ret,0.5))
