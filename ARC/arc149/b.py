import collections
import bisect

def lis(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
    return len(LIS)

N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))

a_array_with_index=[(a,i) for i,a in enumerate(a_array)]
a_array_with_index.sort()
sorted_b_array=[]
for _,i in a_array_with_index:
    sorted_b_array.append(b_array[i])
b_lis=lis(sorted_b_array)
print(N+b_lis)
