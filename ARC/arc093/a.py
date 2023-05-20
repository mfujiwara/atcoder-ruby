N=int(input())
array=list(map(int, input().split()))
total=0
for i in range(N):
    if i==0:
        total+=abs(array[i])
    else:
        total+=abs(array[i]-array[i-1])
total+=abs(array[-1])
for i in range(N):
    pre=0
    if i>0:
        pre=array[i-1]
    post=0
    if i<N-1:
        post=array[i+1]
    v=total-abs(pre-array[i])-abs(post-array[i])+abs(pre-post)
    print(v)
