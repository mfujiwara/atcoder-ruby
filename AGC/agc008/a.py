x,y=map(int, input().split())
if x==y:
    print(0)
elif abs(x)==abs(y):
    print(1)
elif abs(x)>abs(y):
    if x<0:
        if y<=0:
            print(abs(x)-abs(y))
        else:
            print(1+abs(x)-abs(y))
    else:
        if y<=0:
            print(1+abs(x)-abs(y))
        else:
            print(2+abs(x)-abs(y))
else:
    if x<0:
        if y<=0:
            print(abs(y)-abs(x)+2)
        else:
            print(abs(y)-abs(x)+1)
    else:
        if y<=0:
            print(abs(y)-abs(x)+1)
        else:
            print(abs(y)-abs(x))
