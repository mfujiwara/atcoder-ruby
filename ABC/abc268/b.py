S=input()
T=input()
l=len(S)
if len(T)>=l and S==T[:l]:
    print("Yes")
else:
    print("No")
