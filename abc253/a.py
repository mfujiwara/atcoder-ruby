a,b,c=map(int, input().split())
abc=sorted([a,b,c])
if abc[1]==b:
    print("Yes")
else:
    print("No")
