S=input()
N=len(S)+1
rets=[0]*N
for i,ch in enumerate(S):
    if ch=="<":
        rets[i+1]=rets[i]+1
for i,ch in enumerate(S[::-1]):
    if ch==">":
        rets[N-2-i]=max(rets[N-2-i],rets[N-1-i]+1)
print(sum(rets))
