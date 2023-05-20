N=int(input())
array=list(map(int, input().split()))
maxi=0
target=-1
for a in array:
    if maxi<=a:
        maxi=a
    else:
        break
rets=[a for a in array if a!=maxi]
print(*rets)
