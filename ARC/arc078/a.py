import itertools
N=int(input())
array=list(map(int, input().split()))
sums=list(itertools.accumulate(array))
total=sums[-1]
ret=abs(total-2*array[0])
for i in range(1,N-1):
    ret=min(ret,abs(total-2*sums[i]))
print(ret)
