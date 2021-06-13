N,A,B=map(int, input().split())
total=0
maxi=0
mini=10**9
for _ in range(N):
    s=int(input())
    total+=s
    maxi=max(maxi,s)
    mini=min(mini,s)
if (maxi==mini and B!=0) or (maxi!=mini and B==0):
    print(-1)
    exit()
if maxi==mini:
    print(f"{0} {A}")
    exit()
P=B/(maxi-mini)
a=total*P/N
Q=A-a
print(f"{P} {Q}")
