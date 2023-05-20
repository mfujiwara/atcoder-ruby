H,W=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H)]
B=[list(map(int, input().split())) for _ in range(H)]
c=0
for i in range(H-1):
    for j in range(W-1):
        diff=B[i][j]-A[i][j]
        c+=abs(diff)
        A[i][j]+=diff
        A[i+1][j]+=diff
        A[i][j+1]+=diff
        A[i+1][j+1]+=diff
    if A[i][W-1]!=B[i][W-1]:
        print("No")
        exit()
if A[H-1]!=B[H-1]:
    print("No")
    exit()
print("Yes")
print(c)
