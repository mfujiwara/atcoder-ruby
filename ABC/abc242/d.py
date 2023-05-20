S=input()
Q=int(input())
ordA=ord("A")
for _ in range(Q):
    t,k=map(int, input().split())
    k-=1
    bits=[]
    s=min(t,60)
    for _ in range(s):
        k,r=divmod(k,2)
        bits.append(r)
    if s==t:
        ret=ord(S[k])-ordA
    else:
        diff=t-s
        ret=(ord(S[0])-ordA+diff)%3
    while bits:
        b=bits.pop()
        if b==0:
            ret+=1
            ret%=3
        else:
            ret+=2
            ret%=3
    print(chr(ret+ordA))
