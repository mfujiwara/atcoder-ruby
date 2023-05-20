import sys
N=int(input())
array=list(map(int, input().split()))
base_value=0
base_index=-1
for i in range(N):
    if abs(base_value)<abs(array[i]):
        base_value=array[i]
        base_index=i
if base_value==0:
    print(0)
elif base_value>0:
    print(2*N)
    pre=base_index
    for i in range(N):
        print(f"{pre+1} {i+1}")
        print(f"{pre+1} {i+1}")
        pre=i
else:
    print(2*N)
    pre=base_index
    for i in range(N)[::-1]:
        print(f"{pre+1} {i+1}")
        print(f"{pre+1} {i+1}")
        pre=i
