N=int(input())
ranging=0
for _ in range(N):
    s,e=map(int, input().split("-"))
    sq,sr=divmod(s,100)
    eq,er=divmod(e,100)
    sb=sq*12+sr//5
    eb=eq*12+(er+4)//5
    r=((1<<(eb-sb))-1)<<sb
    ranging|=r
rets=[]
rain=False
for i in range(24):
    for j in range(12):
        b=ranging&1
        if rain:
            if b==0:
                rets.append(f"{i:02}{j*5:02}")
                rain=False
        else:
            if b==1:
                rets.append(f"{i:02}{j*5:02}")
                rain=True
        ranging//=2
if rain:
    rets.append("2400")
for i in range(len(rets)//2):
    s=rets[i*2]
    e=rets[i*2+1]
    print(f"{s}-{e}")
