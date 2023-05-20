A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
D=list(map(int, input().split()))
#  (Px - Cx) * (Qy - Cy) - (Py - Cy) * (Qx - Cx)
for a,b,c in [[A,B,C],[B,C,D],[C,D,A],[D,A,B]]:
    s=(a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0])
    if s>0:
        print("No")
        exit()
print("Yes")
