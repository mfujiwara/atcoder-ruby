from operator import pos


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
N,M,Q=map(int, input().split())
txy=[]
y_set=set([0])
for _ in range(Q):
    t,x,y=map(int, input().split())
    txy.append((t,x-1,y))
    y_set.add(y)
sorted_y=sorted(list(y_set))
L=len(y_set)
y2index={}
for i,y in enumerate(sorted_y):
    y2index[y]=i
a_array=[0]*N
b_array=[0]*M
a_tree=Bit(L)
a_tree.add(1,N)
b_tree=Bit(L)
b_tree.add(1,M)
a_sum_tree=Bit(L)
b_sum_tree=Bit(L)
ret=0
for t,x,post_y in txy:
    if t==1:
        pre_y=a_array[x]
        pre_index=y2index[pre_y]
        post_index=y2index[post_y]

        if pre_index>0:
            ret-=b_tree.sum(pre_index)*pre_y
        if pre_index<L:
            ret-=b_sum_tree.sum(L)-b_sum_tree.sum(pre_index)

        a_tree.add(pre_index+1,-1)
        a_sum_tree.add(pre_index+1,-pre_y)
        a_tree.add(post_index+1,1)
        a_sum_tree.add(post_index+1,post_y)

        if post_index>0:
            ret+=b_tree.sum(post_index)*post_y
        if post_index<L:
            ret+=b_sum_tree.sum(L)-b_sum_tree.sum(post_index)

        a_array[x]=post_y
    else:
        pre_y=b_array[x]
        pre_index=y2index[pre_y]
        post_index=y2index[post_y]

        if pre_index>0:
            ret-=a_tree.sum(pre_index)*pre_y
        if pre_index<L:
            ret-=a_sum_tree.sum(L)-a_sum_tree.sum(pre_index)
        b_tree.add(pre_index+1,-1)
        b_sum_tree.add(pre_index+1,-pre_y)
        b_tree.add(post_index+1,1)
        b_sum_tree.add(post_index+1,post_y)

        if post_index>0:
            ret+=a_tree.sum(post_index)*post_y
        if post_index<L:
            ret+=a_sum_tree.sum(L)-a_sum_tree.sum(post_index)

        b_array[x]=post_y
    print(ret)
