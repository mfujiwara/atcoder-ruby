N,K=map(int, input().split())
array=list(map(int, input().split()))
arrays=[[] for _ in range(K)]
for i,a in enumerate(array):
    k=i%K
    arrays[k].append(a)
for i in range(K):
    arrays[i].sort()
for i in range(N-1):
    q0,r0=divmod(i,K)
    q1,r1=divmod(i+1,K)
    if arrays[r0][q0]>arrays[r1][q1]:
        print("No")
        exit()
print("Yes")
