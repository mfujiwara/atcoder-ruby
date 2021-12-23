import heapq
class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heapq.heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heapq.heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res
N,M=map(int, input().split())
S=[[0]*M for _ in range(N)]
flow=MinCostFlow(N*M+2)
s=N*M
t=N*M+1
base=0
k=0
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            S[i][j]=1
        else:
            f=i*M+j
            if ch=="o":
                S[i][j]=2
                flow.add_edge(s,f,1,0)
                base+=N+M-i-j
                k+=1
            flow.add_edge(f,t,1,N+M-i-j)
            if i<N-1:
                flow.add_edge(f,f+M,N*M,0)
            if j<M-1:
                flow.add_edge(f,f+1,N*M,0)
cost=flow.flow(s,t,k)
print(base-cost)
