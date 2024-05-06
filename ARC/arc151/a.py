N=int(input())
S=input()
T=input()
diffs=0
for i in range(N):
    if S[i] != T[i]:
        diffs+=1
if diffs%2 == 1:
    print(-1)
else:
    d=0
    ret=""
    for i in range(N):
        if S[i]==T[i]:
            ret+="0"
        else:
            if abs(d)<diffs:
                ret+="0"
                if S[i]=="0":
                    d-=1
                else:
                    d+=1
            else:
                if d>0:
                    ret+=S[i]
                    d-=1
                else:
                    ret+=T[i]
                    d+=1
            diffs-=1
    print(ret)
