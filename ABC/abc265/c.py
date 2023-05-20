H,W=map(int, input().split())
G=[input() for _ in range(H)]
now=(0,0)
done=set([(0,0)])
while True:
    x,y=now
    if G[x][y]=="U":
        if x==0:
            break
        now=(x-1,y)
    elif G[x][y]=="D":
        if x==H-1:
            break
        now=(x+1,y)
    elif G[x][y]=="L":
        if y==0:
            break
        now=(x,y-1)
    else:
        if y==W-1:
            break
        now=(x,y+1)
    if now in done:
        print(-1)
        exit()
    done.add(now)
print(now[0]+1,now[1]+1)
