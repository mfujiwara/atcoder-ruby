N=int(input())
S=input()
stack=False
for ch in S:
    if ch=="A":
        print("A",end="")
    elif ch=="B":
        if stack:
            print("A",end="")
            stack=False
        else:
            stack=True
    else:
        if stack:
            print("BC",end="")
            stack=False
        else:
            print("C",end="")
if stack:
    print("B")
else:
    print()
