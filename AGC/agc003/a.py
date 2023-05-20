S=input()
news=[False]*4
for ch in S:
    if ch=="N":
        news[0]=True
    elif ch=="E":
        news[1]=True
    elif ch=="W":
        news[2]=True
    else:
        news[3]=True
if not news[0]^news[3] and not news[1]^news[2]:
    print("Yes")
else:
    print("No")
