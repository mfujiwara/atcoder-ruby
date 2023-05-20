K=int(input())
S=input()
memo={}
memo[(0,0)]=[-1,1,1,-1] #LRUD
x,y=0,0
for ch in S:
    ox=x
    oy=y
    if ch=="L":
        while (x,y) in memo:
            x=memo[(x,y)][0]
        memo[(ox,y)][0]=x-1
    elif ch=="R":
        while (x,y) in memo:
            x=memo[(x,y)][1]
        memo[(ox,y)][1]=x+1
    elif ch=="U":
        while (x,y) in memo:
            y=memo[(x,y)][2]
        memo[(x,oy)][2]=y+1
    else:
        while (x,y) in memo:
            y=memo[(x,y)][3]
        memo[(x,oy)][3]=y-1
    memo[(x,y)]=[x-1,x+1,y+1,y-1]
print(x,y)
