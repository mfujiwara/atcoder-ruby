N=int(input())
A=[input() for _ in range(N)]
ret=""
for i in range(N):
    for j in range(N):
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==0 and dy==0: continue
                s=""
                x=i
                y=j
                for k in range(N):
                    s+=A[x][y]
                    x+=dx
                    x%=N
                    y+=dy
                    y%=N
                ret=max(ret,s)
print(ret)
