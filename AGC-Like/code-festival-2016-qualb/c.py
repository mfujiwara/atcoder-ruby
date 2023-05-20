W,H=map(int, input().split())
costs=[]
for i in range(W):
    c=int(input())
    costs.append((c,True,i))
for i in range(H):
    c=int(input())
    costs.append((c,False,i))
costs.sort(key=lambda e:-e[0])
ret=0
h=H+1
w=W+1
while costs:
    c,b,i=costs.pop()
    if b:
        if w>1:
            ret+=c*h
            w-=1
    else:
        if h>1:
            ret+=c*w
            h-=1
print(ret)
