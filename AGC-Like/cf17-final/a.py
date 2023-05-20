S=input()
akiba="AKIHABARA"
c=0
for ch in akiba:
    if len(S)>c and ch==S[c]:
        c+=1
    elif ch=="A":
        continue
    else:
        print("NO")
        exit()
if c==len(S):
    print("YES")
else:
    print("NO")
