N=int(input())
array=list(map(int, input().split()))
maxi=max(array)
if maxi*2<sum(array):
    print("Yes")
else:
    print("No")
