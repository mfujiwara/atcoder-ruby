A,B=map(int, input().split())
a=b=0
while A>0:
    A,r=divmod(A,10)
    a+=r
while B:
    B,r=divmod(B,10)
    b+=r
print(max(a,b))
