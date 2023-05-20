import re
S=input()
for i in range(len("keyence")+1):
    keyence=list("keyence")
    keyence.insert(i,".*")
    keyence="".join(keyence)
    if re.fullmatch(keyence, S):
        print("YES")
        exit()
print("NO")
