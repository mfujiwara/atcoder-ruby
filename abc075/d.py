N,K=map(int, input().split())
xy_dots=[]
x_dots=[]
y_dots=[]
for i in range(N):
    x,y=map(int, input().split())
    xy_dots.append((x,y))
    x_dots.append(x)
    y_dots.append(y)
x_dots=sorted(x_dots)
y_dots=sorted(y_dots)
ret=1<<100
for i in range(N-K+1):
    x1=x_dots[i]
    for j in range(i+K-1,N):
        x2=x_dots[j]
        for k in range(N-K+1):
            y1=y_dots[k]
            for l in range(k+K-1,N):
                y2=y_dots[l]
                c=0
                for x,y in xy_dots:
                    if x1<=x<=x2 and y1<=y<=y2: c+=1
                if c>=K:
                    ret=min(ret,(x2-x1)*(y2-y1))
print(ret)
