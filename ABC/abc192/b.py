import sys
S=input()
for i,ch in enumerate(S):
    is_s= "a" <= ch <= "z"
    if (i%2==0 and not is_s)or(i%2==1 and is_s):
        print("No")
        sys.exit()
print("Yes")
