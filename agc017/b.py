N,A,B,C,D=map(int, input().split())
A,B=0,abs(A-B)
for i in range(N):
    low=(N-1-i)*C-i*D
    high=(N-1-i)*D-i*C
    if low<=B<=high:
        print("YES")
        exit()
print("NO")
