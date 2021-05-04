N=int(input())
members=[]
for _ in range(N):
    a,b,c,d,e=map(int, input().split())
    members.append((a,b,c,d,e))
right=1
left=10**9+1
while True:
    if right+1==left:
        print(right)
        exit()
    mid=(right+left)//2
    mbs=set()
    for member in members:
        mb=(
            1 if member[0]>=mid else 0,
            1 if member[1]>=mid else 0,
            1 if member[2]>=mid else 0,
            1 if member[3]>=mid else 0,
            1 if member[4]>=mid else 0
        )
        mbs.add(mb)
    mbs=list(mbs)
    enable=False
    for m1 in mbs:
        for m2 in mbs:
            for m3 in mbs:
                if (m1[0] or m2[0] or m3[0]) and (m1[1] or m2[1] or m3[1]) and (m1[2] or m2[2] or m3[2]) and (m1[3] or m2[3] or m3[3]) and (m1[4] or m2[4] or m3[4]):
                    enable=True
                    break
            if enable:
                break
        if enable:
            break
    if enable:
        right=mid
    else:
        left=mid
