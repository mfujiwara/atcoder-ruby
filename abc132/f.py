MOD=pow(10,9)+7
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            s %= MOD
            i -= i & -i
        return s

    def add(self, i, x):
        """i=0には足せない"""
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= MOD
            i += i & -i
N,K=map(int, input().split())
array=[]
array2=[]
for i in range(1,N+1):
    j=N//i
    if i<j:
        array.append(i)
        array2.append(j)
    elif i==j:
        array.append(i)
        break
    else:
        break
array+=array2[::-1]
L=len(array)
# array[i-1]より大きくarray[i]以下の場合の数
memo0=[1 if i==0 else array[i]-array[i-1] for i in range(L)]
memo=[1 if i==0 else array[i]-array[i-1] for i in range(L)]
for _ in range(K-1):
    tree=Bit(L+1)
    for i in range(L):
        tree.add(1,memo[i])
        tree.add(L+1-i,-memo[i])
    memo=[tree.sum(i+1)*memo0[i]%MOD for i in range(L)]
print(sum(memo)%MOD)
