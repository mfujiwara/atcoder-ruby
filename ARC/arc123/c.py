T=int(input())
for _ in range(T):
    s=list(map(int,list(input())))
    ret=1
    for k in s:
        if ret==1:
            if 1<=k<=3:
                 continue
            else:
                if 4<=k<=6:
                    ret=2
                elif 7<=k<=9:
                    ret=3
                else:
                    ret=4
                    break
        if ret==2:
            if 2<=k<=6:
                continue
            elif 7<=k<=9:
                ret=3
            else:
                ret=4
                break
        if ret==3:
            if 3<=k<=9:
                continue
            else:
                ret=4
                break
    if 1<=ret<=3:
        print(ret)
        continue
    valid=True
    end=-1
    shift=False
    for k in s[::-1]:
        if shift:
            if k>0:
                k-=1
                shift=False
            else:
                k=9
            
        if end==3:
            if 3<=k<=9:
                continue
            elif k==2:
                end=2
            elif k==1:
                end=1
            else:
                valid=False
                break
        elif end==2:
            if 2<=k<=6:
                continue
            elif k==1:
                end=1
            else:
                valid=False
                break
        elif end==1:
            if 1<=k<=3:
                continue
            else:
                valid=False
                break
        else:
            if k==3:
                end=3
            elif 0<=k<=2:
                shift=True

    if valid:
        print(4)
    else:
        print(5)

            
