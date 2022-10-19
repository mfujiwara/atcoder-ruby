import itertools
N,M=map(int, input().split())
sss=set()
len_sss=0
for _ in range(N):
    s=input()
    sss.add(s)
    len_sss+=len(s)
ttt=set()
for _ in range(M):
    t=input()
    ttt.add(t)
ccc=16-len_sss-N+1
for perm in itertools.permutations(sss):
    targets=[(perm[0],1,ccc)]
    while targets:
        s,i,c=targets.pop()
        if i==N:
            #print("!",s)
            if s not in ttt and len(s)>=3:
                print(s)
                exit()
        else:
            for k in range(c+1):
                targets.append((s+"_"*(k+1)+perm[i],i+1,c-k))
print(-1)
