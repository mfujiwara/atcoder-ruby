import sys
N,M=map(int, input().split())
s=input()
rets=[]
i=N
while i>0:
    if i<=M:
        rets.append(i)
        break
    j=i
    for k in range(M):
        if s[i-M+k]=="0":
            j=i-M+k
            break
    if i==j:
        print(-1)
        sys.exit()
    rets.append(i-j)
    i=j
print(" ".join(map(str,rets[::-1])))
