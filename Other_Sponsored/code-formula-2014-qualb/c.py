import sys
A=input()
B=input()
a=""
b=""
keep=False
keep_check_set=set()
for i in range(len(A)):
    if not keep and A[i] in keep_check_set:
        keep=True
    keep_check_set.add(A[i])
    if A[i]!=B[i]:
        a+=A[i]
        b+=B[i]
n=len(a)
if n==0:
    if keep:
        print("YES")
        sys.exit()
elif 2<=n<=6:
    kouho=[a]
    for x in range(3):
        nexts=[]
        for k in kouho:
            for i in range(n-1):
                for j in range(i+1,n):
                    tmp=list(k)
                    tmp[i],tmp[j]=tmp[j],tmp[i]
                    nexts.append("".join(tmp))
        kouho=nexts
        if (keep or x==2) and b in kouho:
            print("YES")
            sys.exit()
print("NO")
