N=int(input())
minus=[]
plus=[]
equal=[]
for _ in range(N):
    a,b=map(int, input().split())
    if a>b:
        plus.append((a,b))
    elif a<b:
        minus.append((a,b))
    else:
        equal.append((a,b))
minus.sort()
plus.sort(key=lambda e: -e[1])
now=0
ret=0
for a,b in minus+equal+plus:
    now+=a
    ret=max(ret,now)
    now-=b
print(ret)
