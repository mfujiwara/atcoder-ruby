N=int(input())
array=list(map(int, input().split()))

maxi=max(array)
print(array.index(maxi)+1)
