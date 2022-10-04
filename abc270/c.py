N,X,Y=map(int, input().split())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
def calc(s):
    rets=[]
    status=[0]*N
    targets=[0]
    while targets:
        t=targets.pop()
        if status[t]==0:
            status[t]=1
            targets.append(t)
            rets.append(t)
            if s==t:
                return rets
            for u in edges[t]:
                if status[u]==0:
                    targets.append(u)
        else:
            rets.pop()
to_x=calc(X-1)[::-1]
to_y=calc(Y-1)[::-1]
# print(to_x)
# print(to_y)
pre=None
while to_x and to_y and to_x[-1]==to_y[-1]:
    pre=to_x.pop()
    to_y.pop()
rets=to_x+[pre]+to_y[::-1]
print(*[v+1 for v in rets])
