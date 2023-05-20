X=input()
array=[]
total=0
for ch in X:
    a=int(ch)
    array.append(a)
    total+=a
rets=[]
base=total
while array:
    base,r=divmod(base,10)
    rets.append(r)
    total-=array.pop()
    base+=total
if base>0:
    rets.append(base)
while rets:
    print(rets.pop(),end="")
print()
