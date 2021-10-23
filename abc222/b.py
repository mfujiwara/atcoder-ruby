N,P=map(int, input().split())
array=list(map(int, input().split()))
ret=0
for a in array:
    if a<P:
        ret+=1
print(ret)
