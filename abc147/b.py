S=input()
ret=0
for i in range(len(S)//2):
    if S[i]!=S[-1-i]:
        ret+=1
print(ret)
