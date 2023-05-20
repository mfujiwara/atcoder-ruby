N=int(input())
array=list(map(int, input().split()))
total=1
odd=1
for a in array:
    total*=3
    if a%2==0:
        odd*=2
print(total-odd)
