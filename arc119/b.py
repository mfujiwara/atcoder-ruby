N=int(input())
S=input()
T=input()
if S.count("0")!=T.count("0"):
    print(-1)
    exit()
ret=0
diff=0
for i in range(N):
    if diff==0:
        if S[i]=="0" and T[i]=="1":
            diff+=1
        elif S[i]=="1" and T[i]=="0":
            diff-=1
    elif diff>0:
        if S[i]=="0":
            diff+=1
        if T[i]=="0":
            diff-=1
            ret+=1
    elif diff<0:
        if T[i]=="0":
            diff-=1
        if S[i]=="0":
            diff+=1
            ret+=1
print(ret)
