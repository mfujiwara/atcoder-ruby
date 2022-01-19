import itertools
N,L=map(int, input().split())
c=0
for prod in itertools.product([0,1,2],repeat=L-1):
    print("2",end="")
    for p in prod:
        print(p,end="")
    print()
    print("0",end="")
    for p in prod:
        print((p+1)%3,end="")
    print()
    print("1",end="")
    for p in prod:
        print((p+2)%3,end="")
    print()
    c+=1
    if c==N:
        break
