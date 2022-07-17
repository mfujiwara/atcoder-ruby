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
N=int(input())
S=input()
array=list(map(int, input().split()))
sorted_set=sorted(list(set(array)))
mmap={}
for i,w in enumerate(sorted_set):
    mmap[w]=i+1
w_array=[]
for a in array:
    w_array.append(mmap[a])
tree=Bit(len(sorted_set)+1)
for i in range(N):
    ch=S[i]
    w=w_array[i]
    if ch=="0":
        tree.add(w+1,1)
    else:
        tree.add(1,1)
        tree.add(w+1,-1)
ret=0
for i in range(len(sorted_set)+1):
    ret=max(ret,tree.sum(i+1))
print(ret)
