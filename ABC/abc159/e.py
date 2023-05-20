import itertools
import sys
H,W,K=map(int, input().split())
CHOCO=[input() for _ in range(H)]

if H==1:
    r=0
    c=0
    for i in range(W):
        if CHOCO[0][i]=="1": c+=1
        if c==K+1:
            c=1
            r+=1
    print(r)
    sys.exit()

ret=H*W
for prod in itertools.product([True,False], repeat=H-1):
    idxs=[0]
    for p in prod:
        if p: idxs.append(idxs[-1])
        else: idxs.append(idxs[-1]+1)
    cut_count=idxs[-1]
    counts=[0]*(idxs[-1]+1)
    just_cut=True
    j=0
    while j<W:
        cut=False
        for i in range(H):
            idx=idxs[i]
            if CHOCO[i][j]=="1":
                counts[idx]+=1
                if counts[idx]>K:
                    cut=True
        if cut:
            counts=[0]*(idxs[-1]+1)
            cut_count+=1
            if just_cut:
                cut_count=ret
                break
            just_cut=True
        else:
            j+=1
            just_cut=False
    ret=min(ret,cut_count)
print(ret)
