N=int(input())
flowers=[False]*(100001)
ret=0
for _ in range(N):
    a=int(input())
    if flowers[a]:
        ret+=1
    else:
        flowers[a]=True
print(ret)
