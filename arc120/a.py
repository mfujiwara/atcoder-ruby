N=int(input())
array=list(map(int, input().split()))
sums=[0]
for a in array:
    sums.append(sums[-1]+a)
max_num=0
base=0
for i in range(N):
    base+=sums[i+1]
    max_num=max(max_num,array[i])
    print(base+max_num*(i+1))
