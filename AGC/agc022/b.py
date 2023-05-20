N=int(input())
if N==3:
    for a in [2,5,63]:
        print(a)
    exit()
if N==4:
    for a in [2, 5, 20, 63]:
        print(a)
    exit()
if N==5:
    for a in [2, 5, 20, 30, 63]:
        print(a)
    exit()
total=0
rets=[]
for i in range(1,50000):
    if i%2==0 or i%3==0:
        rets.append(i)
        total+=i
        total%=6
        if len(rets)==N:
            break
if total==2:
    rets.remove(8)
    rets.append(30000)
if total==3:
    rets.remove(9)
    rets.append(30000)
if total==5:
    rets.remove(9)
    rets.append(29998)
for r in rets:
    print(r)
