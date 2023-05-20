N=int(input())
array=list(map(int, input().split()))
c=0
for i,a in enumerate(array):
    if array[a-1]==i+1:
        c+=1
print(c//2)
