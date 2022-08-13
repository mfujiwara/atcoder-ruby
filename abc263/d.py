import itertools


N,L,R=map(int, input().split())
array=list(map(int, input().split()))
sums=list(itertools.accumulate(array))
# 左i番目まで変更した時のsums
left=[sums[-1]]
for i in range(N):
    left.append(sums[N-1]-sums[i]+L*(i+1))
#print(left)
# leftのi以下の最小値
left_min=[]
mini=left[0]
for i in range(N+1):
    mini=min(mini,left[i])
    left_min.append(mini)
#print(left_min)
ret=sums[N-1]
# i個右から変えた場合を考えていく
for i in range(N+1):
    if i==N:
        v=i*R
    else:
        v=i*R-(sums[N-1]-sums[N-1-i])+left_min[N-i]
    ret=min(ret,v)
print(ret)
