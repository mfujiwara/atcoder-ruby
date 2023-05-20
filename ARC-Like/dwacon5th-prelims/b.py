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

N,K=map(int, input().split())
array=list(map(int, input().split()))

tree=Bit(N)
for i,a in enumerate(array):
    tree.add(i+1,a)

nums=[]
for i in range(N):
    for j in range(i+1,N+1):
        nums.append(tree.sum(j)-tree.sum(i))        
ret=0
for i in range(42)[::-1]:
    bit=1<<i
    r=ret+bit
    count=0
    for num in nums:
        if r&num==r: count+=1
    if count>=K:
        ret=r
print(ret)
