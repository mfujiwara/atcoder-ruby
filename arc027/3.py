import collections
X,Y=map(int, input().split())
N=int(input())
th=[]
for _ in range(N):
    t,h=map(int, input().split())
    th.append((t,h))
ret=0
memo=collections.defaultdict(int)
memo[(X+Y,0)]=0
for t,h in th: # N<=300
    new_memo=collections.defaultdict(int)
    keys=list(memo.keys())
    for key in keys: # XY<=600
        memo_h=memo[key]
        memo_t,memo_n=key
        if memo_t>=t and memo_n<X:
            new_t=memo_t-t
            new_n=memo_n+1
            new_key=(new_t,new_n)
            new_memo[new_key]=max(memo[new_key],memo[key]+h)
            ret=max(ret,new_memo[new_key])
    memo.update(new_memo)
print(ret)
