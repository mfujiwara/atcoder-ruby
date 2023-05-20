N,D=map(int, input().split())
dd=D*D
ret=0
for _ in range(N):
    x,y=map(int, input().split())
    if x*x+y*y<=dd:
        ret+=1
print(ret)
