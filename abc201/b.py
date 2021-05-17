N=int(input())
h1=("-",0)
h2=("-",0)
for _ in range(N):
    s,t=input().split()
    t=int(t)
    if t>h1[1]:
        h2=h1
        h1=(s,t)
    elif t>h2[1]:
        h2=(s,t)
print(h2[0])
