import heapq
X,Y,Z,K=map(int, input().split())
x_array=list(map(lambda e: int("-"+e), input().split()))
y_array=list(map(lambda e: int("-"+e), input().split()))
z_array=list(map(lambda e: int("-"+e), input().split()))
xy_array=[]
for x in x_array:
    for y in y_array:
        xy_array.append(x+y)
heapq.heapify(xy_array)
xyz_array=[]
for i in range(min(K,len(xy_array))):
    xy=heapq.heappop(xy_array)
    for z in z_array:
        xyz_array.append(xy+z)
heapq.heapify(xyz_array)
for _ in range(K):
    r=heapq.heappop(xyz_array)
    print(abs(r))
