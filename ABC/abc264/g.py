import collections
from itertools import count
INF=pow(10,20)
N=int(input())
ord_a=ord("a")
edges=collections.defaultdict(int)
for _ in range(N):
    t,p=input().split()
    ttt=0
    for ch in t:
        ttt*=100
        ttt+=ord(ch)-ord_a+1
    edges[ttt]=int(p)
#print(edges)
def bellman_ford(s, max_count):
    d = collections.defaultdict(lambda: -INF)
    d[s] = 0
    c = 0
    while True:
        is_update = False
        for u in list(d.keys()):
            if d[u] == -INF: continue
            for ch in range(1,27):
              v=u%100*100+ch
              cost=d[u]+edges[ch]+edges[u*100+ch]+edges[v]
              if cost>d[v]:
                d[v] = cost
                is_update = True
        if not is_update:
            return d
        c += 1
        if c == max_count:
            print("Infinity")
            exit()
ddd=bellman_ford(2727,27*27)
ddd.pop(2727)
#print(ddd)
print(max(ddd.values()))
