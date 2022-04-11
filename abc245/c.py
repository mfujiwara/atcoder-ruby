N,K=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
targets=[a_array[0],b_array[0]]
for i in range(1,N):
    nexts=set()
    for t in targets:
        if abs(t-a_array[i])<=K:
            nexts.add(a_array[i])
        if abs(t-b_array[i])<=K:
            nexts.add(b_array[i])
    targets=nexts
if targets:
    print("Yes")
else:
    print("No")
