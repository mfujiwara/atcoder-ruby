L,R,d=map(int, input().split())
ret=0
for i in range(L,R+1):
    if i%d==0:
        ret+=1
print(ret)
