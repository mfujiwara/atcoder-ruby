N=int(input())
a_array=list(map(int, input().split()))
a_array.sort()
b_array=list(map(int, input().split()))
rets=set()
for a in a_array:
    target=b_array[0] ^ a
    tantative=[]
    for b in b_array:
        tantative.append(target^b)
    tantative.sort()
    if tantative==a_array:
        rets.add(target)
print(len(rets))
rets=list(rets)
rets.sort()
for r in rets:
    print(r)
