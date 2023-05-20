N=int(input())
s=set()
for _ in range(N):
    array=list(map(int, input().split()))
    s.add(tuple(array))
print(len(s))
