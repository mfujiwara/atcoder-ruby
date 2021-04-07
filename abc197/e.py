N=int(input())
balls=[None for _ in range(N)]
for _ in range(N):
    x,c=map(int, input().split())
    c-=1
    if balls[c]==None:
        balls[c]=[x,x]
    else:
        balls[c][0]=min(balls[c][0],x)
        balls[c][1]=max(balls[c][1],x)
balls.append([0,0])
rets=[(0,0)] # (x-pos, len)
for i in range(N+1):
    if balls[i]==None: continue
    ball_min=balls[i][0]
    ball_max=balls[i][1]
    r1=10**20
    r2=10**20
    for rx, rl in rets:
        r1=min(r1,rl+abs(rx-ball_min)+ball_max-ball_min)
        r2=min(r2,rl+abs(rx-ball_max)+ball_max-ball_min)
    rets=[(ball_max,r1),(ball_min,r2)]
print(min(rets[0][1],rets[1][1]))
