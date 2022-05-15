N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
def calc(xy1,xy2,xy3):
    x1,y1=xy1
    x2,y2=xy2
    x3,y3=xy3
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))*4
total=0
for i in range(1,N-1):
    total+=calc(xy[0],xy[i],xy[i+1])
total//=4
ret=total
sub_total=0
next_index=1
# i,i+1 を含む辺で繰り返し
for i in range(N):
    #print("#",sub_total,i,next_index)
    xy1=xy[i]
    for j in range(next_index,next_index+N-2):
        xy2=xy[j%N]
        xy3=xy[(j+1)%N]
        sub_total+=calc(xy1,xy2,xy3)
        #print("+",i,j%N,(j+1)%N)
        ret=min(ret,abs(total-sub_total))
        if sub_total>total:
            sub_total-=calc(xy1,xy2,xy3)
            #print("-",i,j%N,(j+1)%N)
            if sub_total>0:
                sub_total-=calc(xy1,xy2,xy[(i+1)%N])
                #print("-",i,j%N,(i+1)%N)
                next_index=j
            else:
                next_index=j+1
            break
print(ret)
