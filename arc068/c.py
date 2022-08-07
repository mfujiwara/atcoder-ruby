class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        """i=0には足せない"""
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
N,M=map(int, input().split())
# divs[i]:=iの約数一覧
divs = [set() for _ in range(M+1)]
for d in range(1, M+1):
    for i in range(d, M+1, d):
        divs[i].add(d)
l_to_r=[[] for _ in range(M+1)]
r_to_l=[[] for _ in range(M+1)]
for _ in range(N):
    l,r=map(int, input().split())
    l_to_r[l].append(r)
    r_to_l[r].append(l)
rets=[0]*(M+1)
now=0
tree=Bit(M)
# i番目の駅について考える
for i in range(1, M+1):
    # i番目の駅から購入できるものは対象
    now+=len(l_to_r[i])
    tree.add(i, len(l_to_r[i]))
    for d in divs[i]:
        # iの約数の列車は購入可能
        rets[d]+=now
        # 購入済みのものを引く
        rets[d]-=tree.sum(i-d)
    # i番目の駅以降で購入できないものは対象外
    for l in r_to_l[i]:
        now -= 1
        tree.add(l, -1)
for i in range(1, M+1):
    print(rets[i])
