N,M=map(int, input().split())
boxes=[(1,False)]*N
boxes[0]=(1,True)
for _ in range(M):
    x,y=map(int, input().split())
    x-=1
    y-=1
    xn,xb=boxes[x]
    yn,yb=boxes[y]
    boxes[x]=(xn-1,xb if xn>1 else False)
    boxes[y]=(yn+1,xb or yb)
ret=0
for _,b in boxes:
    if b: ret+=1
print(ret)
