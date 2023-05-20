import itertools
N,M=map(int, input().split())
ab=[]
for _ in range(M):
    a,b=map(int, input().split())
    ab.append((a,b))
ab.sort()
cd=[]
for _ in range(M):
    c,d=map(int, input().split())
    cd.append((c,d))
for perm in itertools.permutations([i+1 for i in range(N)],N):
    ef=[]
    for c,d in cd:
        c=perm[c-1]
        d=perm[d-1]
        e=min(c,d)
        f=max(c,d)
        ef.append((e,f))
    ef.sort()
    if ab==ef:
        print("Yes")
        exit()
print("No")
