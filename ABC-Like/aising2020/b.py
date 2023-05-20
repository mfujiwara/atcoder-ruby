N=int(input())
array=list(map(int, input().split()))
ret=0
for i,a in enumerate(array):
    if i%2==0 and a%2==1:
        ret+=1
print(ret)
