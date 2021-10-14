S=input()
T=input()
diff=[]
for i in range(len(S)):
    if S[i]!=T[i]:
        diff.append(i)
if len(diff)==0 or len(diff)==2 and S[diff[0]]==T[diff[1]] and S[diff[1]]==T[diff[0]] and diff[0]==diff[1]-1:
    print("Yes")
else:
    print("No")
