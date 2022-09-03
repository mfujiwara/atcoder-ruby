import heapq
class pqheap:
    def __init__(self):
        self.p = list()
        self.q = list()

    def add(self,x):
        heapq.heappush(self.p, x)

    def remove(self,x):
        heapq.heappush(self.q, x)

    def minimum(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return self.p[0] if len(self.p)>0 else None

    def pop(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return heapq.heappop(self.p) if len(self.p)>0 else None

    def count(self):
        return len(self.p)-len(self.q)

N,K=map(int, input().split())
array=list(map(int, input().split()))
sorted_array=sorted(array)
dic={}
for i,a in enumerate(sorted_array):
    dic[a]=i
left_index=[None]+list(range(N-1))
right_index=list(range(1,N))+[None]
spaces=pqheap()
total_space=0
for i in range(N-1):
    s=sorted_array[i+1]-sorted_array[i]
    spaces.add(-s)
    total_space+=s
ex_spaces=pqheap()
for _ in range(K-1):
    s=-spaces.pop()
    ex_spaces.add(s)
    total_space-=s
print(total_space)
Q=int(input())
for i in range(Q):
    d=int(input())
    a=array[d-1]  
    a_index=dic[a]
    if left_index[a_index]!=None:
        left_a=sorted_array[left_index[a_index]]
    else:
        left_a=None
    if right_index[a_index]!=None:
        right_a=sorted_array[right_index[a_index]]
    else:
        right_a=None
    if left_a==None:
        delete_space=[right_a-a]
        add_space=[]
    elif right_a==None:
        delete_space=[a-left_a]
        add_space=[]
    else:
        delete_space=[a-left_a,right_a-a]
        add_space=[right_a-left_a]
    # update
    if right_index[a_index]!=None:
        left_index[right_index[a_index]]=left_index[a_index]
    if left_index[a_index]!=None:
        right_index[left_index[a_index]]=right_index[a_index]
    sorted_array[a_index]=0
    # N-K-i -> N-K-i-1
    for s in delete_space:
        if ex_spaces.minimum()==None or s<ex_spaces.minimum():
            spaces.remove(-s)
            total_space-=s
        else:
            ex_spaces.remove(s)
    for s in add_space:
        ex_spaces.add(s)
    while ex_spaces.count()!=K-1:
        if ex_spaces.count()>K-1:
            s=ex_spaces.pop()
            spaces.add(-s)
            total_space+=s
        else:
            s=-spaces.pop()
            ex_spaces.add(s)
            total_space-=s
    print(total_space)
    # print("===")
    # print(sorted_array)
    # print(left_index)
    # print(right_index)
    # print(list(spaces))
    # print(left_a,a,right_a)
