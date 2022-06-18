class SegmentTree:
    def __init__(self, init_val, seg_func, ide_ele):
        size = len(init_val)
        self.seg_func = seg_func
        self.ide_ele = ide_ele
        self.n = 1 << (size - 1).bit_length()
        self.node = [ide_ele] * 2 * self.n
        for i in range(size):
            self.node[self.n + i - 1] = init_val[i]
        for i in range(self.n - 2, -1, -1):
            self.node[i] = self.seg_func(self.node[2 * i + 1], self.node[2 * i + 2])

    def update(self, index, val):
        i = index + self.n - 1
        self.node[i] = val
        while i > 0:
            i = int((i - 1)//2)
            l = self.node[2*i+1]
            r = self.node[2*i+2]
            self.node[i] =  self.seg_func(l, r)
  
    def query(self, left, right):
        ret=self.ide_ele
        left+=self.n-1
        right+=self.n-1
        while left<right:
            if left%2==0:
                ret = self.seg_func(ret, self.node[left])
                left+=1
            if right%2==0:
                right-=1
                ret = self.seg_func(ret, self.node[right])
            left=int(left//2)
            right=int(right//2)
        return ret
INF=pow(10,20)
N=int(input())
x_array=list(map(int, input().split()))
c_array=list(map(int, input().split()))
val=[(0,i) for i in range(N)]
for i in range(N):
    x=x_array[i]-1
    c=c_array[i]
    val[x]=(val[x][0]+c,val[x][1])
tree=SegmentTree(val,min,(INF,-1))
ret=0
for _ in range(N):
    #print(val)
    v,index=tree.query(0,N)
    ret+=v
    hate=x_array[index]-1
    hate_v=c_array[index]
    val[hate]=(val[hate][0]-hate_v,val[hate][1])
    val[index]=(INF,-1)
    tree.update(hate,val[hate])
    tree.update(index,(INF,-1))
print(ret)

