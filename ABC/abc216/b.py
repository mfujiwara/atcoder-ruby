N=int(input())
names=set()
for _ in range(N):
    st=input()
    if st in names:
        print("Yes")
        exit()
    else:
        names.add(st)
print("No")
