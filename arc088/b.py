S=input()
l=len(S)
counts=[1]
now=S[0]
for ch in S[1:]:
    if ch==now:
        counts[-1]+=1
    else:
        counts.append(1)
        now=ch
if len(counts)==1:
    print(l)
elif len(counts)==2:
    print(max(counts))
else:
    ret=l
    total=0
    for c in counts:
        total+=c
        ret=min(ret,max(total,l-total))
    print(ret)
