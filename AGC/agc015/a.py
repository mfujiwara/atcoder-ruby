N,A,B=map(int, input().split())
if N==1:
    if A==B:
        print(1)
    else:
        print(0)
elif A>B:
    print(0)
elif A==B:
    print(1)
else:
    mini=A*(N-1)+B
    maxi=A+B*(N-1)
    print(maxi-mini+1)
