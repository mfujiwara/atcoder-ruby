import collections
S=input()
counts=collections.defaultdict(int)
for ch in S:
    counts[ch]+=1
for ch,c in counts.items():
    if c==1:
        print(ch)
        exit()
print(-1)
