N=input()
ret=0
for bit in range(1,pow(2,len(N)-1)):
    a=[]
    b=[]
    n=int(N)
    while n>0:
        n,r=divmod(n,10)
        if bit&1==0:
            a.append(r)
        else:
            b.append(r)
        bit//=2
    a.sort()
    b.sort()
    A=0
    while a:
        A=A*10+a.pop()
    B=0
    while b:
        B=B*10+b.pop()
    ret=max(ret,A*B)
print(ret)
