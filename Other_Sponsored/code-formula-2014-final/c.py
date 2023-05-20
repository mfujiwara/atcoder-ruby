S=input()+" "
rets=set()
name=""
start=False
for ch in S:
    if ch==" ":
        if start and name!="":
            rets.add(name)
        start=False
        name=""
    elif ch=="@":
        if start and name!="":
            rets.add(name)
        start=True
        name=""
    elif start:
        name+=ch
rets=sorted(list(rets))
for ret in rets:
    print(ret)
