N=int(input())
rets=[N]
n=N
while n>0:
    n-=1
    n&=N
    rets.append(n)
while rets:
    print(rets.pop())
