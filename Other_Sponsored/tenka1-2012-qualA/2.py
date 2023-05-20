c=input()
ret=[]
add=False
for ch in c:
    if ch==" ":
        if not add:
            ret.append(",")
            add=True
    else:
        ret.append(ch)
        add=False
print("".join(ret))
