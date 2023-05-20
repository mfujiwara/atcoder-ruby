N,M=map(int, input().split())
array=list(map(int, input().split()))
sums=[0]
sums_b=[0]
for i,a in enumerate(array):
    sums.append(sums[-1]+a)
    sums_b.append(sums_b[-1]+a*(i+1))
ret=-pow(10,20)
for i in range(N-M+1):
    v=sums_b[i+M]-sums_b[i]-(sums[i+M]-sums[i])*i
    ret=max(ret,v)
print(ret)
