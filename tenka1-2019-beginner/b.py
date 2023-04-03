N=int(input())
S=input()
K=int(input())
s=S[K-1]
ret=""
for ch in S:
    if ch==s:
        ret+=s
    else:
        ret+="*"
print(ret)
