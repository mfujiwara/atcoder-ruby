X=input()
x=int(X)
for head in [int(X[0]),int(X[0])+1]:
    for diff in range(-9,10):
        ret=head
        for i in range(len(X)-1):
            r=int(head)+diff*(i+1)
            if not 0<=r<=9:
                break
            ret=ret*10+int(r)
        if ret>=x:
            print(ret)
            exit()
