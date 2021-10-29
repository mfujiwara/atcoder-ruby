X,Y,A,B,C=map(int, input().split())
if X*Y<A+B+C:
    print("No")
    exit()
for a,b,c in [(A,B,C),(B,C,A),(C,A,B)]:
    for x,y in [(X,Y),(Y,X)]:
        x-=(a+y-1)//y
        if x<=0: continue
        x-=(b+y-1)//y
        if x<=0: continue
        if x*y>=c:
            print("Yes")
            exit()
    for x,y in [(X,Y),(Y,X)]:
        x-=(a+y-1)//y
        if x<=0: continue
        y-=(b+x-1)//x
        if y<=0: continue
        if x*y>=c:
            print("Yes")
            exit()
print("No")
