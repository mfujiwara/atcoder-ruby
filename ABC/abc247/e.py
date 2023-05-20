import collections
N,X,Y=map(int, input().split())
array=list(map(int, input().split()))+[X+1]
x_index=collections.deque()
y_index=collections.deque()
ng_index=[-1]
ret=0
for i,a in enumerate(array):
    if a==X:
        x_index.append(i)
    if a==Y:
        y_index.append(i)
    if a>X or a<Y:
        #print(i,x_index,y_index)
        while len(x_index)>0 and len(y_index)>0:
            min_xy=min(x_index[0],y_index[0])
            min_yx=max(x_index[0],y_index[0])
            ret+=(min_xy-ng_index[-1])*(i-min_yx)
            if x_index[0]==min_xy:
                x_index.popleft()
            if y_index[0]==min_xy:
                y_index.popleft()
            ng_index.append(min_xy)
        x_index=collections.deque()
        y_index=collections.deque()
        ng_index.append(i)
print(ret)
