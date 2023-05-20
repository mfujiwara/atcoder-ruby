N=int(input())
NG=[int(input()) for _ in range(3)]
for _ in range(100):
    if N in NG:
        break
    if N-3 not in NG:
        N-=3
    elif N-2 not in NG:
        N-=2
    else:
        N-=1
if N<=0:
    print("YES")
else:
    print("NO")
