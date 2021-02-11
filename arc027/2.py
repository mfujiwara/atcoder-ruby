from collections import defaultdict
N=int(input())
s1=input()
s2=input()
s=s1+s2
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
        self.get_parent(id_x) == self.get_parent(id_y)

    def size(self):
        s=set()
        for x in self.parent:
            s.add(self.get_parent(x))
        return len(s)

char_group=defaultdict(list)
for i,ch in enumerate(s):
    if "0" <= ch <= "9": continue
    char_group[ch].append(i)
union=UnionFind(2*N)
for i in range(N):
    union.unite(i,i+N)
for ch in char_group:
    if len(char_group[ch])<2: continue
    for i in char_group[ch][1:]:
        union.unite(char_group[ch][0],i)

rets=defaultdict(lambda: 10)
for i,ch in enumerate(s):
    parent=union.get_parent(i)
    if "0" <= ch <= "9":
        rets[parent]=1
    elif i==0 or i==N:
        rets[parent]=min(rets[parent],9)
    else:
        rets[parent]=min(rets[parent],10)

ret=1
for key in rets:
    ret*=rets[key]
print(ret)
