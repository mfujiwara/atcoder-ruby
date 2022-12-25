A,B,C=map(int, input().split())
if (A^B^C) in [A,B,C] and  not(A==B==C):
    print("Yes")
else:
    print("No")
