N=int(input())
M=2*N
n=N
x=""
while n>0:
    x+=str(min(4,n))
    n-=4
print(M)
print(x[::-1])
