import collections
N=int(input())
x2y=collections.defaultdict(list)
yy_count=collections.defaultdict(int)
for _ in range(N):
    x,y=map(int, input().split())
    for yy in x2y[x]:
        if y>yy:
            yy_count[(yy,y)]+=1
        else:
            yy_count[(y,yy)]+=1
    x2y[x].append(y)
ret=0
for key in yy_count:
    c=yy_count[key]
    ret+=c*(c-1)//2
print(ret)
