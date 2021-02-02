class Bitree:
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
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N=int(input())
array=list(map(int, input().split()))
bitree=Bitree(N)
r=0
for a in array:
    r+=(bitree.sum(N)-bitree.sum(a+1))
    bitree.add(a+1,1)
print(r)
for i in range(N-1):
    r+=N-1-array[i]*2
    print(r)
