INF=pow(10,10)
N=int(input())
total=0
mini_b=INF
for _ in range(N):
    a,b=map(int, input().split())
    total+=a
    if a>b:
        mini_b=min(mini_b,b)
if mini_b==INF:
    print(0)
else:
    print(total-mini_b)        
