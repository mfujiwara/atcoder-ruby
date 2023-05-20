import bisect
N,Q=map(int, input().split())
array=list(map(int, input().split()))
b_array=[]
for i,a in enumerate(array):
    b_array.append(a-1-i)
for _ in range(Q):
    k=int(input())
    idx=bisect.bisect_left(b_array,k)
    if idx==N:
        print(k+N)
    else:
        print(array[idx]-(b_array[idx]-k)-1)
