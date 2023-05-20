S=input()
T=input()
diff=(ord(S[0])-ord(T[0])+26)%26
for i in range(1,len(S)):
    if (ord(S[i])-ord(T[i])+26)%26!=diff:
        print("No")
        exit()
print("Yes")
