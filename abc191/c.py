H,W=map(int, input().split())
MAP=[ input() for _ in range(H) ]
count=0
pre=False
for i in range(H-1):
    for j in range(1,W-1):
        if MAP[i][j]!=MAP[i+1][j]:
            if not pre:
                count+=1
                pre=True
        else:
            pre=False
    pre=False

for j in range(W-1):
    for i in range(1,H-1):
        if MAP[i][j]!=MAP[i][j+1]:
            if not pre:
                count+=1
                pre=True
        else:
            pre=False
    pre=False
print(count)
