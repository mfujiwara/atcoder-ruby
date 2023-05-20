X,Y=map(int, input().split())
ret=1
while True:
    Y//=2
    if X<=Y:
        ret+=1
    else:
        break
print(ret)
