import itertools
N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_counts=[0]*(N+1)
b_counts=[0]*(N+1)
for a in a_array:
    a_counts[a]+=1
for b in b_array:
    b_counts[b]+=1
for i in range(N+1):
    if a_counts[i]+b_counts[i]>N:
        print("No")
        exit()
a_sums=list(itertools.accumulate(a_counts))
b_sums=list(itertools.accumulate(b_counts))
maxi=0
for i in range(1,N+1):
    maxi=max(maxi,a_sums[i]-b_sums[i-1])
rets=b_array[-maxi:]+b_array[:-maxi]
print("Yes")
print(*rets)
