import math
N=int(input())
x0,y0=map(int, input().split())
x,y=map(int, input().split())
xo=(x0+x)/2
yo=(y0+y)/2
t=math.pi*2/N
# x0-xo + i(y0-yo) * (cos(t) + i*sin(t))
# = 
x_r=(x0-xo)*math.cos(t) - (y0-yo)*math.sin(t) + xo
y_r=(y0-yo)*math.cos(t) + (x0-xo)*math.sin(t) + yo
print(f"{x_r} {y_r}")
