S=list(input())
K=set(list(input()))
unknown=36-len(K)
added=0
ret=len(S)
for c in S:
    if c not in K:
        added+=1
        K.add(c)
ret+=2*added/(added+1)*(unknown-added)
for i in range(added):
    ret+=2*i/(i+1)
print(ret)
