N=int(input())
array=list(map(int, input().split()))
mini=min(array)
maxi=max(array)
left=mini
right=maxi
while right-left>pow(10,-4):
    mid=(right+left)/2
    dp=[0,0]
    for a in array:
        dp=[dp[1],max(dp)+a-mid]
    if max(dp)>=0:
        left=mid
    else:
        right=mid
print(left)
sorted_array=sorted(set(array))
left=0
right=len(sorted_array)
while left+1!=right:
    mid=(left+right)//2
    max_dp=[0,0]
    min_dp=[0,0]
    for a in array:
        max_dp=[max_dp[1],max(max_dp)+(1 if a>=sorted_array[mid] else -1)]
        min_dp=[min_dp[1],min(min_dp)+(-1 if a<=sorted_array[mid] else 1)]
    if max(max_dp)>0 and min(min_dp)<=0:
        left=mid
    else:
        right=mid
print(sorted_array[left])
