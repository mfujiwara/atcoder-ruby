N=int(input())
memo=set()
for _ in range(N):
    a=int(input())
    if a in memo:
        memo.remove(a)
    else:
        memo.add(a)
print(len(memo))
