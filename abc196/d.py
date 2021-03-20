import sys
sys.setrecursionlimit(500000)
H,W,A,B=map(int, input().split())
def calc(space, a, b):
    if a==0:
        return 1
    c=space[0]
    r=0
    if c%W<W-1 and (c+1) in space:
        tmp=space[:]
        tmp.remove(c)
        tmp.remove(c+1)
        r+=calc(tmp,a-1,b)
    if c//W<H-1:
        tmp=space[:]
        tmp.remove(c)
        tmp.remove(c+W)
        r+=calc(tmp,a-1,b)
    if b>0:
        tmp=space[:]
        tmp.remove(c)
        r+=calc(tmp,a,b-1)
    return r
print(calc([i for i in range(H*W)], A, B))
