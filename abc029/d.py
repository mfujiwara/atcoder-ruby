Nstr=input()
N=int(Nstr)
length=len(Nstr)
ret=0
for i,n in enumerate(Nstr[::-1]):
    n=int(n)
    m=10**i
    ret+=N//m//10*m
    if n==1:
        ret+=N%m+1
    elif n>1:
        ret+=m
print(ret)
