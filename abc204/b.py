N=int(input())
array=list(map(int, input().split()))
ret=0
for a in array:
    if a>10:
        ret+=a-10
print(ret)
