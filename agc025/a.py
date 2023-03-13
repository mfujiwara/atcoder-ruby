N=int(input())
ret=pow(10,10)
for a in range(1,N):
    b=N-a
    r=0
    for ch in str(a)+str(b):
        r+=int(ch)
    ret=min(ret,r)
print(ret)
