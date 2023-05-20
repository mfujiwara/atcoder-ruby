N=int(input())
array=list(map(int, input().split()))
X=int(input())
total=sum(array)
q,r=divmod(X,total)
ret=q*N
for i,a in enumerate(array):
    r-=a
    if r<0:
        ret+=i+1
        break
print(ret)
