N,D,H=map(int, input().split())
min_a=H/D
for _ in range(N):
    d,h=map(int, input().split())
    #y=ax+b
    min_a=min(min_a,(H-h)/(D-d))
r=H-min_a*D
r=max(r,0)
print(r)
