H,W=map(int, input().split())
S=[[0]*W for _ in range(H)]
x=[]
y=[]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="o":
            x.append(i)
            y.append(j)
ret=abs(x[0]-x[1])+abs(y[0]-y[1])
print(ret)
