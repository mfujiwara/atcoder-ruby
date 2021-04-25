N=int(input())
S=list(input())
Q=int(input())
fliped=False
for _ in range(Q):
    t,a,b=map(int, input().split())
    if t==1:
        if fliped:
            a=(a-1+N)%(2*N)
            b=(b-1+N)%(2*N)
            S[a],S[b]=S[b],S[a]
        else:
            a-=1
            b-=1
            S[a],S[b]=S[b],S[a]
    else:
        fliped = not fliped
if fliped:
    S=S[N:]+S[:N]
print("".join(S))
