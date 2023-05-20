N,Q=map(int, input().split())
S=input()
head=0
for _ in range(Q):
    t,x=map(int, input().split())
    if t==1:
        head-=x
        head%=N
    else:
        print(S[(head+x-1)%N])
