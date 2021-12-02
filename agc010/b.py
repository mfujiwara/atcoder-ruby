N=int(input())
array=list(map(int, input().split()))
total=sum(array)
q,r=divmod(total,N*(N+1)//2)
if r!=0:
    print("NO")
    exit()
c=0
for i in range(N):
    d=array[i]-array[(i+1)%N]+q
    if d%N!=0 or d<0:
        print("NO")
        exit()
    c+=d//N
if c==q:
    print("YES")
else:
    print("NO")
