ret=[]
for ch in input():
    if ch=="B":
        if ret: ret.pop()
    else:
        ret.append(ch)
print("".join(ret))
