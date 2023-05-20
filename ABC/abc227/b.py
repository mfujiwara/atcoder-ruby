N=int(input())
array=list(map(int, input().split()))
memo=set()
for a in range(1,200):
    for b in range(1,200):
        memo.add(4*a*b+3*a+3*b)
ret=0
for a in array:
    if a not in memo:
        ret+=1
print(ret)
