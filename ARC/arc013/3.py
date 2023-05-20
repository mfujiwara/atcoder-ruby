N=int(input())
nim=0
for _ in range(N):
    XYZ=list(map(int, input().split()))
    M=int(input())
    min_xyz=list(map(int, input().split()))
    max_xyz=min_xyz[:]
    for _ in range(M-1):
        xyz=list(map(int, input().split()))
        for i in range(3):
            min_xyz[i]=min(min_xyz[i],xyz[i])
            max_xyz[i]=max(max_xyz[i],xyz[i])
    for i in range(3):
        nim^=min_xyz[i]
        nim^=(XYZ[i]-max_xyz[i]-1)
if nim==0:
    print("LOSE")
else:
    print("WIN")
