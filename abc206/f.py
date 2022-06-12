from functools import lru_cache
T=int(input())
for _ in range(T):
    N=int(input())
    ranges=[]
    for _ in range(N):
        l,r=map(int, input().split())
        ranges.append((l,r))
    @lru_cache(maxsize=None)
    def calc(l,r):
        s=set([i for i in range(101)])
        for ll,rr in ranges:
            if l<=ll<rr<=r:
                v=calc(l,ll)^calc(rr,r)
                if v in s:
                    s.remove(v)
        return min(s)
    ret=calc(1,100)
    if ret==0:
        print("Bob")
    else:
        print("Alice")
