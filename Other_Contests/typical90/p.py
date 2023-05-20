N=int(input())
A,B,C=map(int, input().split())
ret=9999
for i in range(10000):
    ma=i*A
    if ma>N: break
    for j in range(10000-i):
        rest=N-ma-j*B
        if rest<0: break
        q,r=divmod(rest,C)
        if r==0:
            ret=min(ret,i+j+q)
print(ret)
