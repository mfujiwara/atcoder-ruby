s=input()
t=input()
s=sorted(list(s))
t=sorted(list(t),reverse=True)
if s<t:
    print("Yes")
else:
    print("No")
