N,M=map(int, input().split())
memo=set()
for _ in range(M):
    array=list(map(int, input().split()))
    array=sorted(array[1:])
    for a in array:
        for b in array:
            memo.add((a,b))
if len(memo)==N*N:
    print("Yes")
else:
    print("No")
