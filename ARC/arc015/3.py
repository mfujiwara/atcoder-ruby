import collections
import fractions
N=int(input())
edges=collections.defaultdict(list)
l,m,s=input().split()
maxi=(fractions.Fraction(1,1),l)
mini=(fractions.Fraction(1,1),l)
targets=[(l,fractions.Fraction(1,1))]
done=set([l])
m=fractions.Fraction(int(m),1)
edges[l].append((s,m))
edges[s].append((l,1/m))
for _ in range(N-1):
    l,m,s=input().split()
    m=fractions.Fraction(int(m),1)
    edges[l].append((s,m))
    edges[s].append((l,1/m))
while targets:
    t,tm=targets.pop()
    for u,m in edges[t]:
        if u in done: continue
        done.add(u)
        um=m*tm
        maxi=max(maxi,(um,u))
        mini=min(mini,(um,u))
        targets.append((u,um))
lm,l=maxi
sm,s=mini
print(f"1{s}={lm/sm}{l}")
