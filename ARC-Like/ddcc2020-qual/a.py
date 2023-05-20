X,Y=map(int, input().split())
ret=0
if X==1 and Y==1:
    ret+=400000
for z in [X,Y]:
    if z==1:
        ret+=300000
    elif z==2:
        ret+=200000
    elif z==3:
        ret+=100000
print(ret)
