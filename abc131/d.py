N=int(input())
ba=[]
for _ in range(N):
    a,b=map(int, input().split())
    ba.append((b,a))
ba.sort()
now=0
for b,a in ba:
    now+=a
    if now>b:
        print("No")
        exit()
print("Yes")
