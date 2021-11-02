import fractions
N=int(input())
array=[]
for i in range(N):
    x,y=map(int, input().split())
    if x!=1:
        s=(y,x-1)
    else:
        s=(pow(10,9)+1,1)
    t=(y-1,x)
    array.append((s,t))
def compare(a):
    s,t=a
    y,x=s
    return fractions.Fraction(y,x)
array.sort(key=compare)
ret=0
now=(-1,1)
for s,t in array:
    ty,tx=t
    if ty*now[1]>=now[0]*tx:
        ret+=1
        now=s
print(ret)
