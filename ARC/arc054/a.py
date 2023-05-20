L,X,Y,S,D=map(int, input().split())
if X>=Y:
    if D>S:
        print((D-S)/(X+Y))
    else:
        print((L+D-S)/(X+Y))
else:
    if D>S:
        print(min((D-S)/(X+Y),(L-D+S)/(Y-X)))
    else:
        print(min((L+D-S)/(X+Y),(S-D)/(Y-X)))
