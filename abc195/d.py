N,M,Q=map(int, input().split())
boxes=[]
for _ in range(N):
    w,v=map(int, input().split())
    boxes.append((v,w)) # value, wieht
boxes=sorted(boxes)[::-1]
x_array=list(map(int, input().split()))
xx=[]
for i,x in enumerate(x_array):
    xx.append((x,i)) # capa, index
xx=sorted(xx)
for _ in range(Q):
    xx_copy=xx[:]
    l,r=map(int, input().split())
    for i in range(len(xx_copy)-1,-1,-1):
        x,idx=xx_copy[i]
        if l<=idx+1<=r:
            del xx_copy[i]
    ret=0
    for v,w in boxes:
        t=None
        for i in range(len(xx_copy)):
            x,_=xx_copy[i]
            if x>=w:
                t=i
                ret+=v
                break
        if t!=None:
            del xx_copy[t]
    print(ret)
