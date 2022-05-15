N,M=map(int, input().split())
array=list(map(int, input().split()))
array=array[::-1]+[0]*(2**20-len(array))
rets=[]
# 高速ゼータ変換
for i in range(20):
	for j in range(1<<20):
		if (j>>i)&1:
			array[j]^=array[j^(1<<i)]
print(*array[:-1-M:-1])
