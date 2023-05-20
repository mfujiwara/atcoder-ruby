A,B,C,D=map(int, input().split())
if B>=D*C:
    print(-1)
    exit()
# A+x*B/C*x<=D
# A+x*B<=D*C*x
# A<= x*(C*D-B)
x=(A+C*D-B-1)//(C*D-B)
print(x)
