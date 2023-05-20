import bisect
import itertools
N,Q,X=map(int, input().split())
w_array=list(map(int, input().split()))
w_sums=[0]+list(itertools.accumulate(w_array))
counts=[]
starts={}
start=0
while True:
    starts[start]=len(counts)
    if w_sums[-1]-w_sums[start]>=X:
        index=bisect.bisect_left(w_sums,X+w_sums[start])
        counts.append(index-start)
        start=index%N
    else:
        w_total=w_sums[-1]-w_sums[start]
        c_total=N-start
        q,r=divmod(X-w_total,w_sums[-1])
        w_total+=q*w_sums[-1]
        c_total+=q*N
        if r==0:
            counts.append(c_total)
            start=0
        else:
            index=bisect.bisect_left(w_sums,r)
            counts.append(index+c_total)
            start=index%N
    if start in starts:
        break
heads=counts[:starts[start]]
loops=counts[starts[start]:]
#print(heads,loops)
for _ in range(Q):
    k=int(input())
    k-=1
    if k<len(heads):
        print(heads[k])
    else:
        k-=len(heads)
        k%=len(loops)
        print(loops[k])

