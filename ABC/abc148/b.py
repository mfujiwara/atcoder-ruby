N=int(input())
S,T=input().split()
ret=""
for i in range(N):
    ret+=S[i]+T[i]
print(ret)
