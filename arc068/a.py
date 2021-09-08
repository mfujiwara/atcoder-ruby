x=int(input())
q,r=divmod(x,11)
d=0
if 1<=r<=6:
    d=1
elif 7<=r:
    d=2
print(q*2+d)
