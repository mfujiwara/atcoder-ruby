S=input()
K=int(input())
dot_index=[-1]
for i,ch in enumerate(S):
    if ch==".":
        dot_index.append(i)
dot_index.append(len(S))
if len(dot_index)-2<=K:
    print(len(S))
    exit()
ret=0
for i in range(len(dot_index)-K-1):
    ret=max(ret,dot_index[i+K+1]-dot_index[i]-1)
print(ret)
