N=int(input())
S=input()
if N%2==1:
    print(-1)
    exit()
s1=S[:N//2]
s2=S[-N//2:]
ret=0
for i in range(N//2):
    if s1[i]!=s2[i]:
        ret+=1
print(ret)
