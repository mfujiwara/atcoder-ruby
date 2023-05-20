import sys
import itertools
S1=input()
S2=input()
S3=input()
SSS=list(set(S1+S2+S3))
if len(SSS)>10:
    print("UNSOLVABLE")
    sys.exit()
idxs=[[] for _ in range(3)]
for i,SX in enumerate([S1,S2,S3]):
    for ch in SX:
        for j,s in enumerate(SSS):
            if ch==s:
                idxs[i].append(j)
                break
for perm in itertools.permutations([i for i in range(10)], len(SSS)):
    n=[0,0,0]
    if perm[idxs[0][0]]==0 or perm[idxs[1][0]]==0 or perm[idxs[2][0]]==0:
        continue
    for i,idx in enumerate(idxs):
        for j,id in enumerate(idx):
            n[i]=n[i]*10+perm[id]
    if n[0]+n[1]==n[2]:
        print(n[0])
        print(n[1])
        print(n[2])
        sys.exit()
print("UNSOLVABLE")
