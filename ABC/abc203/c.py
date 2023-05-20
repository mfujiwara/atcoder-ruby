N,K=map(int, input().split())
friends=[]
for _ in range(N):
    a,b=map(int, input().split())
    friends.append((a,b))
friends=sorted(friends)
k=K
now=0
f_c=0
while k>0:
    now+=k
    k=0
    while f_c<N and friends[f_c][0]<=now:
        k+=friends[f_c][1]
        f_c+=1
print(now)
