N=int(input())
array=list(map(int, input().split()))
q,r=divmod(sum(array),N)
if r!=0:
    print(-1)
    exit()
total=0
num=0
ret=0
for a in array:
    num+=1
    total+=a
    if total==q*num:
        ret+=num-1
        num=0
        total=0
print(ret)
