N,X=map(int, input().split())
array=list(map(int, input().split()))
total=sum(array)
mini=min(array)
maxi=max(array)
if total-mini<X:
    print(-1)
elif total-maxi>=X:
    print(0)
else:
    print(X-total+mini+maxi)
