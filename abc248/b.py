A,B,K=map(int, input().split())
ret=0
while A<B:
    A*=K
    ret+=1
print(ret)
 