N=int(input())
ret=1+0+N-1
b=1
b2=2
while b2<=N:
    a,c=divmod(N,b2)
    ret=min(ret,a+b+c)
    b+=1
    b2*=2
print(ret)
