N=int(input())
S=input()
if S[0]!=S[-1]:
    print(1)
    exit()
pre=False
for i in range(1,N):
    now=(S[i]!=S[0])
    if pre and now:
        print(2)
        exit()
    pre=now
print(-1)
