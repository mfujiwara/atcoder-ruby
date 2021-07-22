A,B,C=map(int, input().split())
d1=A-B
d2=B-C
if d1==d2:
    print(0)
    exit()
if A==C:
    if A>B:
        print(A-B)
    else:
        print(2*(B-A))
elif A<C:
    if d1>d2:
        if (C-A)%2==0:
            print((C+A)//2-B)
        else:
            print(1+(C+1+A)//2-B)
    else:
        print(B-d1-C)
else:
    if d1<d2:
        print(B-d1-C)
    else:
        if (C-A)%2==0:
            print((A+C)//2-B)
        else:
            print(1+(A+C+1)//2-B)
