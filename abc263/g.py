import collections
import math
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # nの平方根まで計算する
    m = math.floor(math.sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True
from collections import deque
class FordFulkerson:
    n=1
    g=[[] for i in range(1)]
    pos=[]
    def __init__(self,N):
        self.n=N
        self.g=[[] for i in range(N)]
        self.pos=[]
    def add_edge(self,From,To,cap):
        assert 0<=From and From<self.n
        assert 0<=To and To<self.n
        assert 0<=cap
        m=len(self.pos)
        self.pos.append((From,len(self.g[From])))
        self.g[From].append({"to":To,"rev":len(self.g[To]),"cap":cap})
        self.g[To].append({"to":From,"rev":len(self.g[From])-1,"cap":0})
        return m
    def get_edge(self,i):
        m=len(self.pos)
        assert 0<=i and i<m
        _e=self.g[self.pos[i][0]][self.pos[i][1]]
        _re=self.g[_e["to"]][_e["rev"]]
        return {"from":self.pos[i][0],
                "to":_e["to"],
                "cap":_e["cap"]+_re["cap"],
                "flow":_re["cap"]}
    def edges(self):
        m=len(self.pos)
        result=[]
        for i in range(m):
            result.append(self.get_edge(i))
        return result
    def change_edge(self,i,new_cap,new_flow):
        m=len(self.pos)
        assert 0<=i and i<m
        assert 0<=new_flow and new_flow<=new_cap
        _e=self.g[self.pos[i][0]][self.pos[i][1]]
        _re=self.g[_e["to"]][_e["rev"]]
        _e["cap"]=new_cap-new_flow
        _re["cap"]=new_flow
    def flow(self,s,t,flow_limit=(1<<63)-1):
        assert 0<=s and s<self.n
        assert 0<=t and t<self.n
        level=[0 for i in range(self.n)]
        Iter=[0 for i in range(self.n)]
        que=deque([])
        def bfs():
            for i in range(self.n):level[i]=-1
            level[s]=0
            que=deque([])
            que.append(s)
            while(len(que)>0):
                v=que.popleft()
                for e in self.g[v]:
                    if e["cap"]==0 or level[e["to"]]>=0:continue
                    level[e["to"]]=level[v]+1
                    if e["to"]==t:return
                    que.append(e["to"])
        def dfs(func,v,up):
            if (v==s):return up
            res=0
            level_v=level[v]
            for i in range(Iter[v],len(self.g[v])):
                e=self.g[v][i]
                if (level_v<=level[e["to"]] or self.g[e["to"]][e["rev"]]["cap"]==0):continue
                d=func(func,e["to"],min(up-res,self.g[e["to"]][e["rev"]]["cap"]))
                if d<=0:continue
                self.g[v][i]["cap"]+=d
                self.g[e["to"]][e["rev"]]["cap"]-=d
                res+=d
                if res==up:return res
            level[v]=self.n
            return res
        flow=0
        while(flow<flow_limit):
            bfs()
            if level[t]==-1:break
            for i in range(self.n):Iter[i]=0
            while(flow<flow_limit):
                f=dfs(dfs,t,flow_limit-flow)
                if not(f):break
                flow+=f
        return flow
    def min_cut(self,s):
        visited=[False for i in range(self.n)]
        que=deque([])
        que.append(s)
        while(len(que)>0):
            p=que.popleft()
            visited[p]=True
            for e in self.g[p]:
                if e["cap"] and not(visited[e["to"]]):
                    visited[e["to"]]=True
                    que.append(e["to"])
        return visited
N=int(input())
evens=[]
odds=[]
ab=collections.defaultdict(int)
for _ in range(N):
    a,b=map(int, input().split())
    ab[a]=b
    if a%2==0:
        evens.append(a)
    else:
        odds.append(a)
if ab[1]==0:
    odds.append(1)
flow=FordFulkerson(len(evens)+len(odds)+2)
flow0=FordFulkerson(len(evens)+len(odds)+2)
start=len(evens)+len(odds)
end=start+1
for i,a in enumerate(evens):
    flow.add_edge(start,i,ab[a])
    flow0.add_edge(start,i,ab[a])
for i,a in enumerate(odds):
    flow.add_edge(len(evens)+i,end,ab[a])
    if a!=1:
        flow0.add_edge(len(evens)+i,end,ab[a])
for i,a in enumerate(evens):
    for j,b in enumerate(odds):
        if isPrime(a+b):
            #print("prime",a,b)
            flow.add_edge(i,len(evens)+j,ab[a])
            flow0.add_edge(i,len(evens)+j,ab[a])
v=flow.flow(start,end)
v0=flow0.flow(start,end)
d=v0-v
ret=v0+(ab[1]-d)//2
print(ret)
#print("v",v,v0)
#print(ab)