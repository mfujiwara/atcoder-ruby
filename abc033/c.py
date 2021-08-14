S=input()+"+"
ret=0
zero=False
for ch in S:
    if ch=="0":
        zero=True
    if ch=="+":
        if not zero:
            ret+=1
        else:
            zero=False
print(ret)
