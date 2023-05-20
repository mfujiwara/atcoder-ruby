import sys
N=int(input())
mat=[list(map(int, input().split())) for _ in range(N)]
if N==1:
    print("Yes")
    print(mat[0][0])
    print(0)
    sys.exit()
min_val=10**9
min_col=-1
for i,a in enumerate(mat[0]):
    if a<min_val:
        min_val=a
        min_col=i
b_array=[]
for a in mat[0]:
    b_array.append(a-min_val)
a_array=[]
for i in range(N):
    v=mat[i][0]-b_array[0]
    if v<0:
        print("No")
        sys.exit()
    a_array.append(v)
for i in range(N):
    for j in range(N):
        if mat[i][j]!=a_array[i]+b_array[j]:
            print("No")
            sys.exit()
print("Yes")
print(" ".join(list(map(str, a_array))))
print(" ".join(list(map(str, b_array))))
