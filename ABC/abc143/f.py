import collections


N=int(input())
array=list(map(int,input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
count_vals=sorted(list(counts.values()),reverse=True)

tmp=0
rets=[0]*(N+1)
for i in range(1,N+1):
    # i回操作を行える最大のkを求めていく
	while count_vals and count_vals[-1]<i:
		count_vals.pop()
    # i枚以上あるカードの種類数
	tmp+=len(count_vals)
    # i回操作を行うとき、ある種類のカードは最大i回しか使えないので、
    # 上の総和がi回操作を行える対象になり、iで割ると最大のk
	rets[tmp//i] = i

for i in range(N-1,-1,-1):
	rets[i]=max(rets[i+1],rets[i])
for i in range(1,N+1):
    print(rets[i])
