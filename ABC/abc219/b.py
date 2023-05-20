S1=input()
S2=input()
S3=input()
ret=[]
for ch in input():
    if ch=="1":
        ret.append(S1)
    elif ch=="2":
        ret.append(S2)
    else:
        ret.append(S3)
print("".join(ret))
