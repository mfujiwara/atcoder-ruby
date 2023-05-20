class SegmentTree:
    def __init__(self, size):
        self.n=1
        while self.n < size:
            self.n = self.n*2
        self.node=[0]*2*self.n
  
    def update(self, index, val):
        i = index + self.n - 1
        self.node[i] = val
        while i > 0:
            i = int((i - 1)//2)
            l = self.node[2*i+1]
            r = self.node[2*i+2]
            self.node[i] =  l if l > r else r
  
    def get_max(self, left, right):
        ret=0
        left+=self.n-1
        right+=self.n-1
        while left<right:
            if left%2==0:
                if ret<self.node[left]:
                    ret=self.node[left]
                left+=1
            if right%2==0:
                right-=1
                if ret<self.node[right]:
                    ret=self.node[right] 
            left=int(left//2)
            right=int(right//2)
        return ret
N=int(input())
S=list(input())
Q=int(input())
trees=[SegmentTree(N) for _ in range(26)]
for i,ch in enumerate(S):
    c=ord(ch)-ord("a")
    trees[c].update(i,1)
for _ in range(Q):
    a,b,c=input().split() 
    if a=="1":
        i=int(b)-1
        ci=ord(c)-ord("a")
        org=ord(S[i])-ord("a")
        trees[org].update(i,0)
        trees[ci].update(i,1)
        S[i]=c
    else:
        l=int(b)
        r=int(c)
        print(sum([tree.get_max(l-1,r) for tree in trees]))
