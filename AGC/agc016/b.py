N=int(input())
array=list(map(int, input().split()))
maxi=max(array)
mini=min(array)
if maxi==mini:
    if maxi==N-1 or N>=maxi*2:
        print("Yes")
    else:
        print("No")
elif maxi==mini+1:
    max_count=array.count(maxi)
    min_count=array.count(mini)
    M=N-min_count
    maxim=maxi-min_count
    if maxim>0 and M>=maxim*2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
