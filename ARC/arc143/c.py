N,X,Y=map(int, input().split())
array=list(map(int, input().split()))
remainders=[a%(X+Y) for a in array]
if all([a<X for a in remainders]):
    print("Second")
    exit()
if X<=Y:
    print("First")
    exit()
remainders=[a if a<X else a-X for a in remainders]
if all([a<Y for a in remainders]):
    print("First")
else:
    print("Second")
