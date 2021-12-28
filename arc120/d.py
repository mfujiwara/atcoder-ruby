N=int(input())
array=list(map(int, input().split()))
array_with_index=[]
for i,a in enumerate(array):
    array_with_index.append((a,i))
array_with_index.sort()
first_half=set()
for k in range(N):
    a,i=array_with_index[k]
    first_half.add(i)
stack=0
for i in range(2*N):
    if i in first_half:
        d=1
    else:
        d=-1
    stack+=d
    if d*stack>0:
        print("(",end="")
    else:
        print(")",end="")
print()
