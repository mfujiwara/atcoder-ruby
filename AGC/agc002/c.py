N,L=map(int, input().split())
array=list(map(int, input().split()))
last=-1
for i in range(N-1):
    if array[i]+array[i+1]>=L:
        last=i+1
        break
if last==-1:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,last):
        print(i)
    for i in range(N-1,last,-1):
        print(i)
    print(last)
