MOD=998244353
N=int(input())
# x^2-y^2=(x+y)(x-y)<=N
# x-y=z y=x-z
# (2x-z)z<=N
# x <= (N/z+z)/2
if N==1:
    print(1)
    exit()
ret=0
for i in range(1,N):
    r=(N//i+i)//2-i+1
    if r==0:
        break
    ret+=r
    ret%=MOD
print(ret)
