A,B,C,D,E,F,X=map(int, input().split())
x=X
t=0
while x>0:
    t+=min(x,A)*B
    x-=min(x,A)
    x-=min(x,C)
x=X
a=0
while x>0:
    a+=min(x,D)*E
    x-=min(x,D)
    x-=min(x,F)
if t>a:
    print("Takahashi")
elif a>t:
    print("Aoki")
else:
    print("Draw")
