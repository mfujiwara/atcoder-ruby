s=input()
n=len(s)
si=0
for ch in s:
    si = si << 1
    if ch=="o":
        si+=1
sis=[si]
alli=2**n-1
left_bit=2**(n-1)
for _ in range(n-1):
    nexts=sis[-1]*2
    if (sis[-1] & left_bit)==0:
        sis.append(nexts)
    else:
        sis.append((nexts+1)&alli)

ret=n
for b in range(2**n,2**(n+1)):
    c=0
    r=0
    for i in range(n):
        if ((1<<i)&b)!=0:
            c+=1
            r=r|sis[i]
    if r==alli:
        ret=min(ret,c)
print(ret)
