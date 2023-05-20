import math
L,R=map(int, input().split())
d=R-L
while True:
    x=L
    y=L+d
    while y<=R:
        if math.gcd(x,y)==1:
            print(d)
            exit()
        x+=1
        y+=1
    d-=1
