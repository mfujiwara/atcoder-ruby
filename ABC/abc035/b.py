S=input()
T=int(input())
x=0
y=0
c=0
for ch in S:
    if ch=="L":
        x-=1
    elif ch=="R":
        x+=1
    elif ch=="U":
        y+=1
    elif ch=="D":
        y-=1
    else:
        c+=1
if T==1:
    ret=abs(x)+abs(y)+c
else:
    if abs(x)+abs(y)>c:
        ret=abs(x)+abs(y)-c
    else:
        ret=(c-abs(x)-abs(y))%2
print(ret)
