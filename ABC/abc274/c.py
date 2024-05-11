import sys
sys.setrecursionlimit(500000)

N=int(input())
array=list(map(int, input().split()))
rev=dict()
for i,a in enumerate(array):
    rev[a]=i

s=rev[1]
M=(2*N)+1
rets=[-1]*M
def calc(index,g):
    i=(index+1)*2
    rets[i-1]=g+1
    if i in rev:
        a=rev[i]
        calc(a,g+1)
    j=(index+1)*2+1
    rets[j-1]=g+1
    if j in rev:
        b=rev[j]
        calc(b,g+1)
rets[0]=0
calc(s,0)
for r in rets:
    print(r)
