import heapq
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
array=list(map(int, input().split()))
if N<=2:
    print(0)
    exit()
tree=Bit(N)
for i in range(2,N+1):
    tree.add(i,1)
array_with_index=[]
for i,a in enumerate(array):
    array_with_index.append((a,i))
heapq.heapify(array_with_index)
ret=0
for i in range(N-2):
    a,index=heapq.heappop(array_with_index)
    actual_index=tree.sum(index+1)
    ret+=min(actual_index,N-1-i-actual_index)
    tree.add(index+1,-1)
print(ret)
