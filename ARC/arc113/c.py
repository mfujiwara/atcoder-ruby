S=input()
ret=0
chance_num=[0]*26
pre=None
for i,ch in enumerate(S[::-1]):
    c=ord(ch)-ord("a")
    if pre==c:
        ret+=chance_num[c]
        chance_num=[i]*26
        chance_num[c]=0
    for j in range(26):
        if j!=c: chance_num[j]+=1
    pre=c
print(ret)
