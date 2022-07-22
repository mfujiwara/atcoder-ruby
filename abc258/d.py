N,X=map(int, input().split())
ret=pow(10,20)
base=0
for _ in range(N):
    a,b=map(int, input().split())
    base+=a+b
    X-=1
    ret=min(ret,base+X*b)
    if X==0:
        break
print(ret)
