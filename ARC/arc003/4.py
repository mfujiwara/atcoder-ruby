import random
import time
N,M,K=map(int, input().split())
ng=[[False]*N for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    ng[a][b]=True
    ng[b][a]=True
total=0
ret=0
TIME_LIMIT = 9.9
start_time = time.time()
while True:
    now_time = time.time()
    if now_time - start_time > TIME_LIMIT:
        break
    array=[i for i in range(N)]
    for _ in range(K):
        a,b=random.sample([i for i in range(N)], 2)
        array[a],array[b]=array[b],array[a]
    total+=1
    ok=True
    for i in range(N):
        if ng[array[i]][array[(i+1)%N]]:
            ok=False
            break
    if ok:
        ret+=1
print(ret/total)
