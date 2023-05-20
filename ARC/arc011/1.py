m,n,N=map(int, input().split())
t=0
ret=N
while N+t>=m:
    q,r=divmod(N+t,m)
    t=r
    N=n*q
    ret+=N
print(ret)
