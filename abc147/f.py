import collections
N,X,D=map(int, input().split())
if D==0:
    if X==0:
        print(1)
    else:
        print(N+1)
    exit()
if D<0:
    D=-D
    X=-X
ranges=collections.defaultdict(lambda: collections.defaultdict(int))
for i in range(N+1):
    m=i*X%D
    #left=(X+X+D*(i-1))*i//2//D
    #right=(X+D*(N-i)+X+D*(N-1))*i//2//D
    left=X*i//D+i*(i-1)//2
    right=X*i//D+(2*N-1-i)*i//2
    #print(left,right)
    ranges[m][left]+=1
    ranges[m][right+1]-=1
#print(ranges)
ret=0
for rr in ranges.values():
    c=0
    pre=0
    for key,val in sorted(rr.items()):
        if c>0:
            key
            ret+=key-pre
        pre=key
        c+=val
print(ret)
