S=input()
upper=False
lower=False
memo=set()
for ch in S:
    if ch in memo:
        print("No")
        exit()
    memo.add(ch)
    if "A"<=ch<="Z":
        upper=True
    if "a"<=ch<="z":
        lower=True
if upper and lower:
    print("Yes")
else:
    print("No")
