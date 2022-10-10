N,Q=map(int, input().split())
arrays=[]
for _ in range(N):
    array=list(map(int, input().split()))
    arrays.append(array)
for _ in range(Q):
    s,t=map(int, input().split())
    print(arrays[s-1][t])
