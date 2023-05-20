N,K=map(int, input().split())
a_array=list(map(int, input().split()))
f_array=list(map(int, input().split()))
a_array=sorted(a_array)
f_array=sorted(f_array)[::-1]
right=-1
left=a_array[-1]*f_array[0]
while right+1<left:
    mid=(right+left)//2
    k=0
    for i in range(N):
        k+=max(a_array[i]-(mid//f_array[i]),0)
    if k<=K:
        left=mid
    else:
        right=mid
print(left)
