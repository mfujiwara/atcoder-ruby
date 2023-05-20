import bisect
N,K=map(int, input().split())
points=[]
for _ in range(N):
    p_array=list(map(int, input().split()))
    points.append(sum(p_array))
sorted_poinsts=sorted(points)
pp=sorted_poinsts[-K]
for p in points:
    if p>=pp-300:
        print("Yes")
    else:
        print("No")
