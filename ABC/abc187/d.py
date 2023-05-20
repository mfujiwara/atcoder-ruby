N=int(input())
target=0
diffs=[]
for _ in range(N):
    a,b=map(int, input().split())
    target+=a
    diffs.append(2*a+b)
diffs.sort()
while target>=0:
    target-=diffs.pop()
print(N-len(diffs))
