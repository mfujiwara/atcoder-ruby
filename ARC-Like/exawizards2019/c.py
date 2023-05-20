N,Q=map(int, input().split())
memo=[-2]*N
def calc(start, s, tds):
    if memo[start]!=-2:
        return memo[start]
    now=start
    for t,d in tds:
        if s[now]==t:
            now+=d
            if now==-1 or now==len(s):
                memo[start]=now
                return now
    memo[start]=now
    return now
s=list(map(ord,list(input())))
tds=[]
for _ in range(Q):
    t,d=input().split()
    t=ord(t)
    d=-1 if d=="L" else 1
    tds.append((t,d))
calc(0,s,tds)
if memo[0]==N:
    print(0)
    exit()
memo[N-1]=calc(N-1,s,tds)
if memo[N-1]==-1:
    print(0)
    exit()
if memo[0]>=0 and memo[N-1]<=N-1:
    print(N)
    exit()
left_side=-1
if memo[0]==-1:
    left=0
    right=N-1
    while True:
        if left+1==right:
            left_side=left
            break
        mid=(left+right)//2
        v=calc(mid,s,tds)
        if v==-1:
            left=mid
        else:
            right=mid
right_side=N
if memo[N-1]==N:
    left=0
    right=N-1
    while True:
        if left+1==right:
            right_side=right
            break
        mid=(left+right)//2
        v=calc(mid,s,tds)
        if v==N:
            right=mid
        else:
            left=mid
print(right_side-left_side-1)
