import collections
import heapq
N,M,K,L=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
edges=collections.defaultdict(list)
for _ in range(M):
    u,v,c=map(int, input().split())
    u-=1
    v-=1
    edges[u].append((v,c))
    edges[v].append((u,c))

size=N
INF=pow(10,10)

# done[i]:=人iと友達になった人気者の国の集合. 最大2つまで考えればok
done=[set() for _ in range(size)]
# shortest[i][j]:=人iと国jに属する人気者が友達になる最小コスト
shortest=[collections.defaultdict(lambda: INF) for _ in range(size)]

queue=[]
for b in b_array:
    b-=1
    a=a_array[b]
    shortest[b][a]=0
    queue.append((0,b,a))
heapq.heapify(queue)

while queue:
    #print(queue)
    #print(queue[0])
    cost,u,country = heapq.heappop(queue)    
    if shortest[u][country]<cost or len(done[u])>=2: continue
    done[u].add(country)

    for v,c in edges[u]:
        if country in done[v] or len(done[v])>=2: continue
        a = shortest[u][country] + c
        if a < shortest[v][country]:
            shortest[v][country]=a
            heapq.heappush(queue, (a,v,country))
rets=[INF]*N
for i in range(N):
    for country,cost in shortest[i].items():
        if country!=a_array[i]:
            rets[i]=min(rets[i],cost)
print(*[ret if ret!=INF else -1 for ret in rets])
#print(shortest)
