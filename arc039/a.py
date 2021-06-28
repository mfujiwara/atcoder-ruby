A,B=input().split()
ret=int(A)-int(B)
for i in range(30):
    x=i%10
    y=i//10
    if y==0 and x==0:
        continue
    a=list(A)
    a[y]=str(x)
    a=int("".join(a))
    ret=max(ret,int(a)-int(B))
for j in range(30):
    m=j%10
    n=j//10
    if m==0 and n==0:
        continue
    b=list(B)
    b[n]=str(m)
    b=int("".join(b))
    ret=max(ret,int(A)-int(b))
print(ret)
