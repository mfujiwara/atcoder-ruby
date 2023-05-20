N,X=map(int, input().split())
array=list(map(int, input().split()))
total=0
for i,a in enumerate(array):
    if i%2==0:
        total+=a
    else:
        total+=a-1
if total>X:
    print("No")
else:
    print("Yes")
