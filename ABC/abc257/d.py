import heapq
INF=pow(10,10)
N=int(input())
xyp=[]
for _ in range(N):
    x,y,p=map(int, input().split())
    xyp.append((x,y,p))
# X[i][j]:=i番目からj番目にジャンプするときに必要なS
X=[[INF]*N for _ in range(N)]
for i in range(N):
    xi,yi,p=xyp[i]
    for j in range(N):
        if i==j: continue
        xj,yj,_=xyp[j]
        s=(abs(xi-xj)+abs(yi-yj)+p-1)//p
        X[i][j]=s
#print(X)
ret=INF
for i in range(N):
    #print("start",i)
    done=set()
    targets=[(0,i)]
    rr=0
    while targets:
        s,t=heapq.heappop(targets)
        #print(s,t)
        rr=max(rr,s)
        if t not in done:
            done.add(t)
            if len(done)==N:
                break
        else:
            continue
        for u in range(N):
            if u in done: continue
            if X[t][u]<=s:
                heapq.heappush(targets,(s,u))
            else:
                heapq.heappush(targets,(X[t][u],u))
    ret=min(ret,rr)
print(ret)
