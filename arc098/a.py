N=int(input())
S=input()
sumsE=[0]*N
sumsW=[0]*N
for i,ch in enumerate(S):
    if i>0:
        sumsW[i]=sumsW[i-1]
    if ch=="W":
        sumsW[i]+=1
for i,ch in list(enumerate(S))[::-1]:
    if i<N-1:
        sumsE[i]=sumsE[i+1]
    if ch=="E":
        sumsE[i]+=1
sums=[0]*N
for i in range(N):
    if i==0:
        sums[i]=sumsE[i+1]
    elif i==N-1:
        sums[i]=sumsW[i-1]
    else:
        sums[i]=sumsE[i+1]+sumsW[i-1]
print(min(sums))
