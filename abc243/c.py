N=int(input())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
S=input()
memo={}
for i,ch in enumerate(S):
    if ch=="R":
        x,y=xy[i]
        if y in memo:
            memo[y]=min(memo[y],x)
        else:
            memo[y]=x
for i,ch in enumerate(S):
    if ch=="L":
        x,y=xy[i]
        if y in memo and memo[y]<x:
            print("Yes")
            exit()
print("No")
