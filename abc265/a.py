X,Y,N=map(int, input().split())
ret=X*N
for y in range((N+3)//3):
    v=y*Y+(N-3*y)*X
    ret=min(ret,v)
print(ret)
