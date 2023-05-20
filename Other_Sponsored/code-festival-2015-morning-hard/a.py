N=int(input())
array=list(map(int, input().split()))
ret=0
left_ret=[0]
left_count=array[:1]
for i in range(N-1):
    left_ret.append(left_ret[-1]+left_count[-1])
    left_count.append(left_count[-1]+array[i+1]+1)
right_ret=[0]
right_count=array[-1:]
for i in range(N-1):
    right_ret.append(right_ret[-1]+right_count[-1])
    right_count.append(right_count[-1]+array[-2-i]+1)
ret=left_ret[-1]
for i in range((N-1)//2+1):
    ret=min(ret,right_ret[i*2]+left_ret[-1-i*2])
print(ret)
