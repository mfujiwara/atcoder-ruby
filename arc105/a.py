A,B,C,D=sorted(list(map(int, input().split())))
if A+B+C==D or A+D==B+C:
    print("Yes")
else:
    print("No")
