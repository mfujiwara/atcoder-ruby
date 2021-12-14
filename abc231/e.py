import collections
N,X=map(int, input().split())
array=list(map(int, input().split()))
def calc(x):
    ret=0
    for a in array[::-1]:
        q,x=divmod(x,a)
        ret+=q
        if x==0:
            break
    return ret
targets=collections.defaultdict(lambda: pow(10,20))
targets[X]=0
for i in range(N-1):
    nexts=collections.defaultdict(lambda: pow(10,20))
    a=array[i]
    b=array[i+1]
    for x in targets:
        c=targets[x]
        r=x%b
        if r==0:
            nexts[x]=min(nexts[x],c)
        else:
            x_n=x-r
            nexts[x_n]=min(nexts[x_n],c+r//a)
            x_p=x-r+b
            nexts[x_p]=min(nexts[x_p],c+(b-r)//a)
    targets=nexts
ret=min([targets[x]+x//array[-1] for x in targets])
print(ret)
