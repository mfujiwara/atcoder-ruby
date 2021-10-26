INF=pow(10,9)
T=int(input())
for _ in range(T):
    r,g,b=map(int, input().split())
    ret=INF
    for c1,c2 in [(r,g),(g,b),(b,r)]:
        if abs(c1-c2)%3==0:
            ret=min(ret,max(c1,c2))
    if ret==INF:
        print(-1)
    else:
        print(ret)
