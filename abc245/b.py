N=int(input())
array=list(map(int, input().split()))
s=set(array)
ret=0
while ret in s:
    ret+=1
print(ret)
