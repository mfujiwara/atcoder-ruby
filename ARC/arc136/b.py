N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_counts=[0]*5001
b_counts=[0]*5001
for a in a_array:
    a_counts[a]+=1
for b in b_array:
    b_counts[b]+=1
if a_counts!=b_counts:
    print("No")
    exit()
if max(a_counts)>1:
    print("Yes")
    exit()
for i in range(N-2):
    b=b_array[i]
    a_index=a_array.index(b)
    if a_index%2==0:
        a_array.pop(a_index)
    else:
        a_array.pop(a_index)
        a_array[0],a_array[1]=a_array[1],a_array[0]
if b_array[-2]==a_array[0] and b_array[-1]==a_array[1]:
    print("Yes")
else:
    print("No")

