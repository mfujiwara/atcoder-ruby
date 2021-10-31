N,M=map(int, input().split())
B=[list(map(int, input().split())) for _ in range(N)]
s=B[0][0]%7
if s==0:
    s=7
t=B[0][-1]%7
if t==0:
    t=7
if s>t:
    print("No")
    exit()   
for i in range(M-1):
    if B[0][i]+1!=B[0][i+1]:
        print("No")
        exit()        
for j in range(N-1):
    if B[j][0]+7!=B[j+1][0]:
        print("No")
        exit()
for i in range(1,N):
    for j in range(1,M):
        if B[i][j-1]+1!=B[i][j]:
            print("No")
            exit()
print("Yes")
