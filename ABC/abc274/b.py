H,W=map(int, input().split())
rets=[0]*W
for _ in range(H):
    s=input()
    for i in range(W):
        if s[i]=="#":
            rets[i]+=1
print(*rets)
