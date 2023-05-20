import sys
sys.setrecursionlimit(500000)
class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
 
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
 
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
M,N=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(M)]
B=[list(map(int, input().split())) for _ in range(M)]
s=M*N
g=s+1
ford=FordFulkerson(M*N+2)
diff=0
for i in range(M):
    for j in range(N):
        if (i+j)%2==0:
            ford.add_edge(s,i*N+j,1)
        else:
            ford.add_edge(i*N+j,g,1)
        if A[i][j]!=B[i][j]:
            diff+=1
for i in range(M):
    for j in range(N-1):
        if A[i][j]!=A[i][j+1] and A[i][j]!=B[i][j] and A[i][j]==B[i][j+1]:
            if (i+j)%2==0:
                fr=i*N+j
                to=i*N+j+1
            else:
                fr=i*N+j+1
                to=i*N+j
            ford.add_edge(fr,to,1)
for i in range(M-1):
    for j in range(N):
        if A[i][j]!=A[i+1][j] and A[i][j]!=B[i][j] and A[i][j]==B[i+1][j]:
            if (i+j)%2==0:
                fr=i*N+j
                to=(i+1)*N+j
            else:
                fr=(i+1)*N+j
                to=i*N+j
            ford.add_edge(fr,to,1)
flow=ford.flow(s,g)
ret=diff-flow
print(ret)
