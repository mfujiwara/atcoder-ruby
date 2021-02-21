import sys
N=int(input())
S=[input() for _ in range(N)]
depth=[None]*N
depth[0]=0
targets=[0]
d=1
while targets:
    nexts=[]
    for target in targets:
        for i in range(N):
            if S[target][i]=="0": continue
            if depth[i]==None:
                depth[i]=d
                nexts.append(i)
            else:
                if depth[i]%2!=d%2:
                    print("-1")
                    sys.exit()
    targets=nexts
    d+=1
INF=1<<60
def warshall_floyd(node_size):
    d = [[INF]*node_size for _ in range(node_size)]
    for u in range(N):
        for v in range(N):
            if S[u][v]=="0": continue
            d[u][v]=1
    for k in range(node_size):
        for i in range(node_size):
            for j in range(node_size):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
d=warshall_floyd(N)
ret=0
for i in range(N-1):
    for j in range(i+1,N):
        ret=max(ret,d[i][j])
print(ret+1)
