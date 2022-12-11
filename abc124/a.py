A,B=map(int, input().split())
if A==B:
    print(A+B)
else:
    C=max(A,B)
    print(2*C-1)
