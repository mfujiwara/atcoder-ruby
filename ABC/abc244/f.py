import collections
INF=pow(10,10)
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
#print(edges)
rets=[INF]*pow(2,N)

done=[[False]*N for _ in range(pow(2,N))]
done[0]=[True]*N
done_bit=set()
shortest=[[INF]*N for _ in range(pow(2,N))]
shortest[0]=[0]*N
queue=collections.deque()
for i in range(N):
    bit=pow(2,i)
    shortest[bit][i]=1
    queue.append((1,bit,i))

while len(queue)>0 and len(done_bit)<pow(2,N):
    #print(queue)
    #print(*shortest,sep="\n")
    cost, bit,u = queue.popleft()
    if shortest[bit][u]<cost: continue
    done[bit][u] = True    #探されたuは確定
    done_bit.add(bit)

    for v in edges[u]:
        v_bit=bit^pow(2,v)
        if done[v_bit][v]: continue
        a = shortest[bit][u] + 1
        if a < shortest[v_bit][v]:
            shortest[v_bit][v]=a
            queue.append((a,v_bit,v))
ret=0
for s in shortest:
    ret+=min(s)
print(ret)
