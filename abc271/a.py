N=int(input())
a,b=divmod(N,16)
if a>=10:
    a=chr(ord("A")+a-10)
else:
    a=str(a)
if b>=10:
    b=chr(ord("A")+b-10)
else:
    b=str(b)
print(a+b)
