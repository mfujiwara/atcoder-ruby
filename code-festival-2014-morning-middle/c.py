p,n=input().split()
p=float(p)
n=int(n)
if p==1:
    if n%2==0:
        print(0)
    else:
        print(1)
    exit()
ret=(1-pow(1-2*p,n))/2
print(ret)
