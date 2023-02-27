H,N=map(int, input().split())
array=list(map(int, input().split()))
if H<=sum(array):
    print("Yes")
else:
    print("No")
