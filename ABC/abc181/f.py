import math
from typing import Union
class UnionFind:
    def __init__(self, size):
        self.rank = [0]*size
        self.parent = [i for i in range(size)]

    def unite(self, id_x, id_y):
        x_parent = self.get_parent(id_x)
        y_parent = self.get_parent(id_y)
        if x_parent == y_parent:
            return 
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[x_parent] = y_parent
            if self.rank[x_parent] == self.rank[y_parent]:
                self.rank[y_parent] += 1 

    def get_parent(self, id_x):
        if self.parent[id_x] == id_x:
            return id_x
        else:
            self.parent[id_x] = self.get_parent(self.parent[id_x])
            return self.parent[id_x]

    def is_same_parent(self, id_x, id_y):
        return self.get_parent(id_x) == self.get_parent(id_y)

    def size(self):
        s=set()
        for x in self.parent:
            s.add(self.get_parent(x))
        return len(s)
N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
distances=[]
for i in range(N):
    for j in range(i+1,N+2):
        x1,y1=xy[i]
        if j<N:
            x2,y2=xy[j]
            d=math.hypot(x1-x2,y1-y2)
            distances.append((d,i,j))
        elif j==N:
            distances.append((100-y1,i,j))
        else:
            distances.append((y1+100,i,j))
distances.sort()
union=UnionFind(N+2)
for d,i,j in distances:
    union.unite(i,j)
    if union.is_same_parent(N,N+1):
        print(d/2)
        exit()
