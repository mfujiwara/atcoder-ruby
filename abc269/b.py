a,b,c,d=10,0,10,0
for i in range(10):
    for j,ch in enumerate(input()):
        if ch=="#":
            a=min(a,i)
            b=max(b,i)
            c=min(c,j)
            d=max(d,j)
print(a+1,b+1)
print(c+1,d+1)
