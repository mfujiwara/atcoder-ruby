N=int(input())
array=list(map(int, input().split()))
left=0
right=N-1
flip=False
while left<=right:
    zero=1 if flip else 0
    if array[right]==zero:
        right-=1
    elif array[left]==zero:
        left+=1
        flip=not flip
    else:
        print("No")
        exit()
print("Yes")
