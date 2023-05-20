S=input()
K=int(input())
SS=S+S
SSS=S+S+S
def count(s):
    pre="_"
    ret=0
    for ch in s:
        if pre==ch:
            ret+=1
            pre="_"
        else:
            pre=ch
    return ret
c=count(S)
cc=count(SS)
ccc=count(SSS)
if cc-c==ccc-cc:
    print(c+(cc-c)*(K-1))
else:
    q,r=divmod(K-1,2)
    print(c+(ccc-c)*q+(cc-c)*r)
