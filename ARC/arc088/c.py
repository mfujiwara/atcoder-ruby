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
import collections
S=input()
L=len(S)
odd_count=0
indexes=collections.defaultdict(list)
for i,ch in enumerate(S):
    indexes[ch].append(i)
    if len(indexes[ch])%2==0:
        odd_count-=1
    else:
        odd_count+=1
if odd_count>1:
    print(-1)
    exit()
half1=[]
mid=[]
half2=[]
for ch,idxs in indexes.items():
    l=len(idxs)
    if l%2==0:
        half1+=idxs[:l//2]
        half2+=idxs[l//2:]
    else:
        half1+=idxs[:l//2]
        half2+=idxs[l//2+1:]
        mid=idxs[l//2:l//2+1]
half1.sort()
half2.sort()
tree=Bit(L)
sortedS=half1+mid+half2
# 配列を一致させるswap回数
def calc(a1,a2):
    #print(a1,a2)
    a1=[-1]+a1
    a2=[-1]+a2
    index={}
    for i,a in enumerate(a1):
        index[a]=i
    tree=Bit(len(a1))
    diff=0
    for i in range(len(a2)-1,0,-1):
        a=a2[i]
        to=i
        fr0=index[a]
        fr=fr0-tree.sum(fr0)
        tree.add(fr0,1)
        diff+=to-fr
    return diff
# 前半後半で分割するまでの操作回数
ret=calc([i for i in range(L)],sortedS)
#print(ret)
indexes2=collections.defaultdict(collections.deque)
for i,idx in enumerate(half1):
    ch=S[idx]
    indexes2[ch].append(i)
half22=[]
for i,idx in enumerate(half2):
    ch=S[idx]
    half22.append(indexes2[ch].pop())
# 前半と後半を一致させるための操作回数
ret2=calc([L//2-1-i for i in range(L//2)],half22)
print(ret+ret2)
