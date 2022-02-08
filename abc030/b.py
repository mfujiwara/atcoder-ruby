N,M=map(int, input().split())
x=N*30+M/2
y=M*6
ret=min(abs(x-y)%360,360-abs(x-y)%360)
print(ret)
