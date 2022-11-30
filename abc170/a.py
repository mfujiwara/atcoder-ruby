x=list(map(int, input().split()))
for i,a in enumerate(x,1):
    if a==0:
        print(i)
        exit()
