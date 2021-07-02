N=int(input())
s=input()
t=input()
if s==t:
    print(N)
    exit()
for i in range(N):
    x=s+t[-1-i:]
    if x[-N:]==t:
        print(N+i+1)
        exit()
