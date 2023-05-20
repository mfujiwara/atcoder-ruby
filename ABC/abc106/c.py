S=input()
K=int(input())
for i,ch in enumerate(S):
    if ch!="1":
        break
if K<=i:
    print("1")
else:
    print(ch)
