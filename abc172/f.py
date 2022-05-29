from functools import lru_cache


N=int(input())
array=list(map(int, input().split()))
diff=0
for i in range(2,N):
    diff^=array[i]
a0=array[0]
a1=array[1]
memo={}
@lru_cache(maxsize=None)
def calc(a0,a1,i):
    if i==0:
        #print(a0,a1,a0^a1,diff)
        if a0^a1==diff&1:
            return 0
        else:
            return -1
    d=(diff>>i)&1
    d0=(a0>>i)&1
    d1=(a1>>i)&1
    #print(i,d,d0,d1,a0,a1,a0^a1)
    mask=(1<<i)-1
    if d==d0^d1:
        rrr=calc(a0&mask,a1&mask,i-1)
        if rrr!=-1:
            return rrr
        if d0==1 and d1==0:
            r0=(a0&mask)+1
            r1=(1<<i)-(a1&mask)
            r=max(r0,r1)
            rrr=calc((a0-r)&mask,(a1+r)&mask,i-1)
            if rrr==-1:
                return -1
            else:
                return rrr+r
        return -1
    if d==0:
        if d0==1: # d1==0
            r0=(a0&mask)+1
            r1=(1<<i)-(a1&mask)
            if r0==r1:
                return -1
            r=min(r0,r1)
        else: # d0==0 d1==1
            return -1
    else:
        if d0==1: # d1==1
            r=(a0&mask)+1
            if r>(1<<i)-(a1&mask):
                return -1
        else: # d0==0 d1==0
            r=(1<<i)-(a1&mask)
            if r>(a0&mask):
                return -1
    #print(ret)
    rrr=calc((a0-r)&mask,(a1+r)&mask,i-1)
    if rrr==-1:
        return -1
    else:
        return rrr+r
ret=calc(a0,a1,40)
if ret==a0:
    print(-1)
else:
    print(ret)
