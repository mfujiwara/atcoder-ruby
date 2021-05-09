MOD=7
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
N=int(input())
S=input()
X=input()
mod=set()
mod.add(0)
base=1
for i in range(N)[::-1]:
    s=int(S[i])
    x=X[i]
    if x=="T":
        tmp=set(mod)
        if s!=0:
            for m in mod:
                p=(70+m-base*s)%7
                tmp.add(p)
    else:
        tmp=set()
        # x+s*base in mod
        # x+0 in mod
        for i in range(7):
            if (i+s*base)%7 in mod and i in mod:
                tmp.add(i)
        if len(tmp)==0:
            print("Aoki")
            exit()
    base=base*10%7
    mod=tmp
if 0 in mod:
    print("Takahashi")
else:
    print("Aoki")
