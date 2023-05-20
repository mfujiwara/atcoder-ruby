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
        ret=-2
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

N,M=map(int, input().split())
diffs=[0]*(N+2)
st=[]
for _ in range(M):
    s,t=map(int, input().split())
    st.append((s,t))
    diffs[s]+=1
    diffs[t+1]-=1
tree=SegmentTree(N+1)
v=0
for i in range(1,N+1):
    v+=diffs[i]
    tree.update(i, -v)
rets=[]
for i in range(M):
    s,t=st[i]
    v=tree.get_max(s,t+1)
    if v<-1:
        rets.append(i+1)
print(len(rets))
for r in rets:
    print(r)
