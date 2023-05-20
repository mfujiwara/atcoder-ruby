N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
ret=0
for i in range(N):
    ret+=a_array[i]*b_array[i]
if ret==0:
    print("Yes")
else:
    print("No")
