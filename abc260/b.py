N,X,Y,Z=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
done=[False]*N

array=[]
for i,p in enumerate(a_array):
    array.append((-p,i))
array.sort(reverse=True)
for _ in range(X):
    _,i=array.pop()
    done[i]=True

array=[]
for i,p in enumerate(b_array):
    if done[i]: continue
    array.append((-p,i))
array.sort(reverse=True)
for _ in range(Y):
    _,i=array.pop()
    done[i]=True

array=[]
for i in range(N):
    if done[i]: continue
    array.append((-a_array[i]-b_array[i],i))
array.sort(reverse=True)
for _ in range(Z):
    _,i=array.pop()
    done[i]=True

for i in range(N):
    if done[i]:
        print(i+1)
