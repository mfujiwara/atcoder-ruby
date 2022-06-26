import networkx
N,M,K=map(int, input().split())
C=input().split()
P='~'
I={}
D={}
G=networkx.DiGraph()
for _ in range(M):
    a,b=map(int, input().split())
    G.add_edge(a,b)
for comp in networkx.strongly_connected_components(G):
    M-=1
    U=D[M]=[l*P for l in range(N+1)]
    T=''
    for t in comp:
        I[t]=M
    for x in sorted(C[t-1] for t in comp)+[P]:
        for s in[s for v in{I[v]for t in comp for v in G[t]}for s in D[v]if(M<v)*(s<P)]+['']:
            q=len(s:=T+s)
            U[q]=min(U[q],s)
        T+=x
print([-1,A:=min([[D[V][K]for V in D]+[P],C][K<2])][P>A])
