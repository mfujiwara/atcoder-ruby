ss=input().split()
N=int(input())
ngs=[input() for _ in range(N)]
rets=[]
for s in ss:
    allow=True
    for ng in ngs:
        same=True
        if len(ng)==len(s):
            for i in range(len(ng)):
                if s[i]!=ng[i] and ng[i]!="*":
                    same=False
                    break
        else:
            same=False
        if same:
            allow=False
            break
    if allow:
        rets.append(s)
    else:
        rets.append("*"*len(s))
print(" ".join(rets))
