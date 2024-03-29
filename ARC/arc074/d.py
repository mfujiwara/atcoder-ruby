class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
 
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
 
    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)
 
    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
 
    def flow(self, s, t):
        flow = 0
        f = INF = 10**9 + 7
        N = self.N 
        while f:
            self.used = [0]*N
            f = self.dfs(s, t, INF)
            flow += f
        return flow
H,W=map(int, input().split())
flow=FordFulkerson(H+W+2)
sss=H+W
ttt=H+W+1
A=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="o":
            A[i][j]=1
            flow.add_multi_edge(i,H+j,1,1)
        elif ch=="S":
            si=i
            sj=j
            flow.add_edge(sss,i,100)
            flow.add_edge(sss,H+j,100)
        elif ch=="T":
            ti=i
            tj=j
            flow.add_edge(i,ttt,100)
            flow.add_edge(H+j,ttt,100)
if si==ti or sj==tj:
    print(-1)
    exit()
print(flow.flow(sss,ttt))
