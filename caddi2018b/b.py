N,H,W=map(int, input().split())
ret=0
for _ in range(N):
    a,b=map(int, input().split())
    if a>=H and b>=W:
        ret+=1
print(ret)
