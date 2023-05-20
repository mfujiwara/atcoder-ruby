S=input()
ret=0
now=0
for ch in S:
    if ch=="R":
        now+=1
        ret=max(ret,now)
    else:
        now=0
print(ret)
