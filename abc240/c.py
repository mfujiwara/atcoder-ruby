N,X=map(int, input().split())
memo=set([0])
for _ in range(N):
    nexts=set()
    a,b=map(int, input().split())
    for m in memo:
        if m+a<=X:
            nexts.add(m+a)
        if m+b<=X:
            nexts.add(m+b)
    memo=nexts
if X in memo:
    print("Yes")
else:
    print("No")
