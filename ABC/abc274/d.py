N,x,y=map(int, input().split())
array=list(map(int, input().split()))
diffx=[]
diffy=[]
for i in range(1,N):
    if i%2==0:
        diffx.append(array[i])
    else:
        diffy.append(array[i])
x-=array[0]
now=set([0])
for x0 in diffx:
    next=set()
    for x1 in now:
        if x1+x0-x<=10000:
            next.add(x1+x0)
        if x1-x0-x<=10000:
            next.add(x1-x0)
    now=next
if x not in now:
    print("No")
    exit()
now=set([0])
for y0 in diffy:
    next=set()
    for y1 in now:
        if y1+y0-y<=10000:
            next.add(y1+y0)
        if y1-y0-y<=10000:
            next.add(y1-y0)
    now=next
if y not in now:
    print("No")
    exit()
print("Yes")
