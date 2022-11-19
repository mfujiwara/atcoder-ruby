N=int(input())
array=list(map(int, input().split()))
c=0
for a in array:
    if a%2==1:
        c+=1
if c%2==0:
    print("YES")
else:
    print("NO")
