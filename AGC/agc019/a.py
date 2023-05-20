Q,H,S,D=map(int, input().split()) # 1, 2, 4, 8
N=int(input())*4
prices=sorted([(8*Q,1,Q),(4*H,2,H),(2*S,4,S),(D,8,D)])
ret=0
n=N
for _,norm,p in prices:
    q,n=divmod(n,norm)
    ret+=q*p
print(ret)
