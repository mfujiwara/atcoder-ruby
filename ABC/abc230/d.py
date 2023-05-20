import collections
N,D=map(int, input().split())
walls=[]
for _ in range(N):
    l,r=map(int, input().split())
    walls.append((l,r))
walls.sort(key=lambda e:-e[1])
ret=0
while walls:
    l,r=walls.pop()
    p=r+D-1
    ret+=1
    while walls and walls[-1][0]<=p:
        walls.pop()
print(ret)
