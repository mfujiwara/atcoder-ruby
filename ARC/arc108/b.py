N=int(input())
S=input()
memo=["",""]
for ch in S:
    if ch=="x":
        if memo[-2]=="f" and memo[-1]=="o":
            memo.pop()
            memo.pop()
        else:
            memo.append(ch)
    else:
        memo.append(ch)
print(len(memo)-2)
