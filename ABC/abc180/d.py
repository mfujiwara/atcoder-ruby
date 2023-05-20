X,Y,A,B=map(int, input().split())
ret=0
while X*A<=X+B and X*A<Y:
    ret+=1
    X*=A
ret+=(Y-X-1)//B
print(ret)
