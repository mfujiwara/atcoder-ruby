S=input()
ret=0
for i in range(10000):
    s=str(i).zfill(4)
    b=True
    for n in range(10):
        ns=str(n)
        if S[n]=="o":
            if s.count(ns)==0:
                b=False
                break
        elif S[n]=="x":
            if s.count(ns)>0:
                b=False
                break
    if b:
        ret+=1
print(ret)
